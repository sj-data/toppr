#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license."""

import telerun
import logging 
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Greetings User, Please use /sub to create a video")

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sub = ",".join(context.args)
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=(f"Creating video for {sub}"))
    telerun.run(sub)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open("./final/final.mp4", 'rb'), filename=f'video.mp4')


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I AM ERROR")


if __name__ == '__main__':
    application = ApplicationBuilder().token('#INSERT ACCESS TOKEN').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
   
    start_handler = CommandHandler('sub', sub)
    application.add_handler(start_handler)

    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()
