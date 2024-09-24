#!/usr/bin/env python3

import configparser
import html
import json
import qrcode
import tempfile
import urllib.parse
import uuid

from datetime import datetime, timezone, timedelta

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import (
    filters,
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
)

from database import create_tables, database, User, Hour
from xray import add_vless_user, query_traffic, remove_vless_user, XrayController, RpcError


config = configparser.ConfigParser()
config.read("config.ini")

BOT_TOKEN = config["telegram"]["bot_token"]
SUPER_USER_ID = int(config["telegram"]["super_user_id"])

XRAY_CONFIG_PATH, API_ADDRESS, API_PORT = config["xray"].values()
ADDRESS, PORT, PATH, REMARKS = config["uri"].values()

XRAY_CTL = XrayController(api_address=API_ADDRESS, api_port=API_PORT)


(
    EMAIL,
    START_OVER,
    ATTRIBUTES,
    SELECTING_ATTRIBUTE,
    CURRENT_ATTRIBUTE,
    TYPING,
    ADDING_USER,
    SELECTING_USER,
    SHOWING,
    REMOVING_USER,
    PERSISTENT,
) = map(chr, range(11))

END = ConversationHandler.END


async def update_traffic_stats(context: ContextTypes.DEFAULT_TYPE) -> None:
    current_hour = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)

    traffic = query_traffic(XRAY_CTL.ss_client, None, True)

    for record in traffic.stat:
        if not record.name.startswith("user>>>"):
            continue

        _, email, _, direction = record.name.split(">>>")

        user = User.get_or_none(User.email == email)
        if not user:
            continue

        rx = record.value if direction == "downlink" else 0
        tx = record.value if direction == "uplink" else 0

        hour_record, created = Hour.get_or_create(
            user=user,
            date=current_hour,
            defaults={"rx": rx, "tx": tx}
        )
        if not created:
            hour_record.rx += rx
            hour_record.tx += tx
            hour_record.save()


async def prune_old_records(context: ContextTypes.DEFAULT_TYPE) -> None:
    time_threshold = datetime.now() - timedelta(hours=24)

    Hour.delete().where(Hour.date < time_threshold).execute()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = (
        "You may choose to add a user or select a user to show their data or remove "
        "them. To abort, simply type /stop.\n\nThe following are the current users:\n"
    )

    query = User.select(User.email)

    buttons = [[InlineKeyboardButton(text="+", callback_data=str(ADDING_USER))]]

    for i, user in enumerate(query):
        text += f"\n{i}. <i>{user.email}</i>"
        button = InlineKeyboardButton(text=str(i), callback_data=user.email)
        if len(buttons[-1]) < 5:
            buttons[-1].append(button)
        else:
            buttons.append([button])

    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    context.user_data[START_OVER] = False
    return SELECTING_USER


async def select_attribute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    buttons = [
        [
            InlineKeyboardButton(text="Update email", callback_data=str(EMAIL)),
            InlineKeyboardButton(text="Toggle persistence", callback_data=str(PERSISTENT)),
        ],
        [
            InlineKeyboardButton(text="Done", callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    attributes = context.user_data.setdefault(ATTRIBUTES, {PERSISTENT: True})

    text = (
        "Customize the attributes to your liking. Once you're done, simply hit 'Done' to create the user."
        "\n\nThe following are the current values:"
        f"\n\nEmail: {attributes.get(EMAIL, '-')}"
        f"\nPersistent: {attributes[PERSISTENT]}"
    )

    if not context.user_data.get(START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_ATTRIBUTE


def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


async def show_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    user = User.get(User.email==update.callback_query.data)

    context.user_data[REMOVING_USER] = user

    current_hour = datetime.now(timezone.utc).replace(microsecond=0, second=0, minute=0)

    text = (
        f"Email:\n - {user.email}"
        f"\nTraffic Usage (hourly, UTC):"
    )

    current_date = None
    for record in user.hours.order_by(Hour.date.asc()):
        record_date_str = record.date[:10]

        if record_date_str != current_date:
            current_date = record_date_str
            text += f"\n {current_date}"

        text += (
            f"\n  {record.date[11:16]} - "
            f"down: {sizeof_fmt(record.rx)}, "
            f"up: {sizeof_fmt(record.tx)}"
        )

    if not user.hours.exists():
        text += "\n - No traffic: user never connected."


    buttons = [
        [
            InlineKeyboardButton(text="Remove", callback_data=str(REMOVING_USER)),
            InlineKeyboardButton(text="Back", callback_data=str(END))
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    context.user_data[START_OVER] = True
    return SHOWING


async def ask_for_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    context.user_data[CURRENT_ATTRIBUTE] = update.callback_query.data
    text = "Okay, tell me."

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)

    return TYPING


async def save_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    user_data = context.user_data
    user_data[ATTRIBUTES][user_data[CURRENT_ATTRIBUTE]] = update.message.text

    user_data[START_OVER] = True

    return await select_attribute(update, context)


async def toggle_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    current_attribute = update.callback_query.data
    context.user_data[ATTRIBUTES][current_attribute] ^= True

    return await select_attribute(update, context)


async def adding_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    if not (email:=context.user_data[ATTRIBUTES].get(EMAIL)):
        await update.callback_query.answer("Email address cannot be empty.")
        return

    if User.select().where(User.email==email).exists():
        await update.callback_query.answer("This email address is already in use by another user.")
        return

    persistent = context.user_data[ATTRIBUTES][PERSISTENT]
    uuid_ = str(uuid.uuid4())

    User.create(email=email, persistent=persistent)
    add_vless_user(client=XRAY_CTL.hs_client, uuid=uuid_, level=0, in_tag="vless", email=email)

    if persistent:
        with open(XRAY_CONFIG_PATH, "r") as handle:
            xray_config = json.load(handle)

        vless_inbound, = [inbound for inbound in xray_config["inbounds"] if inbound["tag"] == "vless"]
        vless_inbound["settings"]["clients"].append({"id": uuid_, "email": email})

        with open(XRAY_CONFIG_PATH, "w") as handle:
            json.dump(xray_config, handle, indent=4)

    uri = (
        f"vless://{uuid_}@{ADDRESS}:{PORT}?path={urllib.parse.quote_plus(PATH)}"
        f"&security=tls&encryption=none&type=ws#{REMARKS}-{email}"
    )
    text = f"Here is the URI for user \"{email}\":\n\n<code>{html.escape(uri)}</code>"

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, parse_mode=ParseMode.HTML)

    qr = qrcode.make(uri)
    with tempfile.NamedTemporaryFile(suffix=".png") as handle:
        qr.save(handle.name)

        await update.effective_message.reply_document(document=handle)

    return END


async def removing_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    user = context.user_data.pop(REMOVING_USER)

    try:
        remove_vless_user(client=XRAY_CTL.hs_client, in_tag="vless", email=user.email)
    except RpcError as e:
        text = f"Failed to remove VLESS user:\n\n<pre>{html.escape(str(e))}</pre>"
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, parse_mode=ParseMode.HTML)
        context.user_data[START_OVER] = False
        return END

    user.delete_instance()
    if user.persistent:
        with open(XRAY_CONFIG_PATH, "r") as handle:
            xray_config = json.load(handle)

        vless_inbound, = [inbound for inbound in xray_config["inbounds"] if inbound["tag"] == "vless"]
        vless_inbound["settings"]["clients"][:] = [c for c in vless_inbound["settings"]["clients"] if c["email"] != user.email]

        with open(XRAY_CONFIG_PATH, "w") as handle:
            json.dump(xray_config, handle, indent=4)

    await update.callback_query.answer("Removed user")
    return await start(update, context)


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Okay, bye.")

    return END


async def post_init(application: Application):
    database.connect()

    with open(XRAY_CONFIG_PATH, "r") as handle:
        xray_config = json.load(handle)

    vless_inbound, = [inbound for inbound in xray_config["inbounds"] if inbound["tag"] == "vless"]
    for client in vless_inbound["settings"]["clients"]:
        User.get_or_create(email=client["email"], defaults={"persistent": True})


async def post_shutdown(application: Application):
    database.close()


def main() -> None:
    create_tables()

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start, filters=filters.User(SUPER_USER_ID))],
        states={
            SELECTING_USER: [
                CallbackQueryHandler(select_attribute, pattern="^" + str(ADDING_USER) + "$"),
                CallbackQueryHandler(show_data, pattern="^(?!" + str(ADDING_USER) + ").*$"),
            ],
            SELECTING_ATTRIBUTE: [
                CallbackQueryHandler(toggle_input, pattern="^" + str(PERSISTENT) + "$"),
                CallbackQueryHandler(ask_for_input, pattern="^(?!" + str(END) + ").*$"),
                CallbackQueryHandler(adding_user, pattern="^" + str(END) + "$"),
            ],
            SHOWING: [
                CallbackQueryHandler(removing_user, pattern="^" + str(REMOVING_USER) + "$"),
                CallbackQueryHandler(start, pattern="^" + str(END) + "$")
            ],
            TYPING: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_input)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    application.add_handler(conv_handler)

    job_queue = application.job_queue
    job_queue.run_repeating(update_traffic_stats, interval=timedelta(minutes=5), first=10)
    job_queue.run_repeating(prune_old_records, interval=timedelta(hours=1), first=20)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
