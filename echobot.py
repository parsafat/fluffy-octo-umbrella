#!/usr/bin/env python3

from telegram.constants import ParseMode
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    filters,
    ConversationHandler,
    CallbackQueryHandler,
    MessageHandler,
)

from xray import *
from database import *

import uuid
import html
import urllib.parse
from datetime import datetime

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

TOKEN = config["bot"]["token"]
ADDRESS, PORT, PATH, REMARKS = config["xray"].values()

XRAY_CTL = XrayController(api_address="127.0.0.1", api_port=10085)


(
    EMAIL,
    START_OVER,
    ATTRIBUTES,
    SELECTING_ATTRIBUTE,
    CURRENT_ATTRIBUTE,
    TYPING,
    ADDING_USER,
    SELECTING_ACTION,
) = map(chr, range(8))

END = ConversationHandler.END


async def save_traffic_stats(context: ContextTypes.DEFAULT_TYPE):
    traffic = query_traffic(XRAY_CTL.ss_client)

    for record in traffic.stat:
        scope, name, _, direction = record.name.split(">>>")

        if scope == "user":
            user, _ = User.get_or_create(email=name)
            TrafficStats.create(user=user, value=record.value, direction=direction, date=datetime.now())


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    text = "You may choose to add a user. To abort, simply type /stop."

    buttons = [
        [
            InlineKeyboardButton(text="Add user", callback_data=str(ADDING_USER)),
        ],
        [
            InlineKeyboardButton(text="Done", callback_data=str(END)),
        ],
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    if context.user_data.get(START_OVER):
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_ACTION


async def select_attribute(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    buttons = [
        [
            InlineKeyboardButton(text="Email", callback_data=str(EMAIL)),
            InlineKeyboardButton(text="Done", callback_data=str(END)),
        ]
    ]
    keyboard = InlineKeyboardMarkup(buttons)

    if not context.user_data.get(START_OVER):
        context.user_data[ATTRIBUTES] = {}
        text = "Please select an attribute to update."

        await update.callback_query.answer()
        await update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
    else:
        text = "Got it! Please select an attribute to update."
        await update.message.reply_text(text=text, reply_markup=keyboard)

    context.user_data[START_OVER] = False
    return SELECTING_ATTRIBUTE


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


async def adding_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    try:
        uuid_ = str(uuid.uuid4())
        email = context.user_data[ATTRIBUTES][EMAIL]

        User.create(email=email)
        add_vless_user(client=XRAY_CTL.hs_client, uuid=uuid_, level=0, in_tag="vless", email=email)

        uri = (
            f"vless://{uuid_}@{ADDRESS}:{PORT}?path={urllib.parse.quote_plus(PATH)}"
            f"&security=tls&encryption=none&type=ws#{REMARKS}-{email}"
        )
        text = f"Here is the URI for user \"{email}\":\n\n<pre>{html.escape(uri)}</pre>"
    except RpcError as e:
        text = f"Failed to add VLESS user:\n\n<pre>{html.escape(str(e))}</pre>"

    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text, parse_mode=ParseMode.HTML)

    return END


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Okay, bye.")

    return END


async def post_init(application: Application):
    database.connect()


async def post_shutdown(application: Application):
    database.close()


def main() -> None:
    create_tables()

    application = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .post_shutdown(post_shutdown)
        .build()
    )

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            SELECTING_ACTION: [
                CallbackQueryHandler(select_attribute, pattern="^" + str(ADDING_USER) + "$"),
            ],
            SELECTING_ATTRIBUTE: [
                CallbackQueryHandler(ask_for_input, pattern="^(?!" + str(END) + ").*$"),
                CallbackQueryHandler(adding_user, pattern="^" + str(END) + "$"),
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
