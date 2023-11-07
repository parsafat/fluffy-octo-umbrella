#!/usr/bin/env python3

import configparser
import html
import json
import urllib.parse
import uuid

from influxdb_client import Point
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync
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

from database import create_tables, database, User
from xray import add_vless_user, query_traffic, remove_vless_user, XrayController


config = configparser.ConfigParser()
config.read("config.ini")

BOT_TOKEN = config["bot"]["token"]
XRAY_CONFIG_PATH, ADDRESS, PORT, PATH, REMARKS = config["xray"].values()
INFLUXDB_TOKEN, ORG, URL, BUCKET= config["influxdb"].values()

with open(XRAY_CONFIG_PATH, "r") as handle:
    xray_config = json.load(handle)

XRAY_CTL = XrayController(api_address="127.0.0.1", api_port=10085)


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
    INFLUXDB_ASYNC_CLIENT,
) = map(chr, range(12))

END = ConversationHandler.END


async def save_traffic_stats(context: ContextTypes.DEFAULT_TYPE):
    write_api = context.bot_data[INFLUXDB_ASYNC_CLIENT].write_api()

    traffic = query_traffic(XRAY_CTL.ss_client)

    for record in traffic.stat:
        scope, name, _, direction = record.name.split(">>>")

        if scope == "user" and (user:=User.select().where(User.email==name)).exists():
            point = (
                Point("traffic-stats")
                .tag("email", name)
                .tag("direction", direction)
                .field("value", record.value)
            )
            await write_api.write(bucket=BUCKET, org=ORG, record=point)


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
    query_api = context.bot_data[INFLUXDB_ASYNC_CLIENT].query_api()

    user = User.get(User.email==update.callback_query.data)

    context.user_data[REMOVING_USER] = user

    query_template = '''
        from(bucket: "{bucket}")
        |> range(start: 0)
        |> filter(fn: (r) => r._measurement == "traffic-stats")
        |> filter(fn: (r) => r.email == "{email}")
        |> filter(fn: (r) => r.direction == "{direction}")
        |> last()
    '''

    query_downlink = query_template.format(bucket=BUCKET, email=user.email, direction="downlink")
    query_uplink = query_template.format(bucket=BUCKET, email=user.email, direction="uplink")

    [[most_recent_downlink]] = (await query_api.query(query_downlink, org=ORG)).to_values(columns=["_value"]) or [[0]]
    [[most_recent_uplink]] = (await query_api.query(query_uplink, org=ORG)).to_values(columns=["_value"]) or [[0]]

    text = (
        f"Email:\n - {user.email}"
        f"\nTraffic Usage (since last Xray restart):"
        f"\n - {sizeof_fmt(most_recent_downlink)} downlink, {sizeof_fmt(most_recent_uplink)} uplink"
    )

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
    try:
        uuid_ = str(uuid.uuid4())
        email = context.user_data[ATTRIBUTES][EMAIL]
        persistent = context.user_data[ATTRIBUTES][PERSISTENT]

        User.create(email=email, persistent=persistent)
        add_vless_user(client=XRAY_CTL.hs_client, uuid=uuid_, level=0, in_tag="vless", email=email)

        if persistent:
            vless_inbound, = [inbound for inbound in xray_config["inbounds"] if inbound["tag"] == "vless"]
            vless_inbound["settings"]["clients"].append({"id": uuid_, "email": email})

            with open(XRAY_CONFIG_PATH, "w") as handle:
                json.dump(xray_config, handle, indent=4)

        uri = (
            f"vless://{uuid_}@{ADDRESS}:{PORT}?path={urllib.parse.quote_plus(PATH)}"
            f"&security=tls&encryption=none&type=ws#{REMARKS}-{email}"
        )
        text = f"Here is the URI for user \"{email}\":\n\n<code>{html.escape(uri)}</code>"
    except RpcError as e:
        text = f"Failed to add VLESS user:\n\n<pre>{html.escape(str(e))}</pre>"

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, parse_mode=ParseMode.HTML)

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

    application.bot_data[INFLUXDB_ASYNC_CLIENT] = InfluxDBClientAsync(url=URL, token=INFLUXDB_TOKEN, org=ORG)

    vless_inbound, = [inbound for inbound in xray_config["inbounds"] if inbound["tag"] == "vless"]
    for client in vless_inbound["settings"]["clients"]:
        User.get_or_create(email=client["email"], defaults={"persistent": True})


async def post_shutdown(application: Application):
    database.close()
    application.bot_data[INFLUXDB_ASYNC_CLIENT].close()


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
        entry_points=[CommandHandler("start", start)],
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
    job_queue.run_repeating(save_traffic_stats, interval=300, first=10)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
