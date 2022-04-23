#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from telegram import ParseMode, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, CallbackContext
from time import strftime, localtime

bot_token = "INSERT TOKEN HERE"

#/start sent by user
def start(update, context):
    textMessage = ("Hello there human!\U0001f44b\U0001f601\n"
                   "The available commands\U0001f4d6 are:\n\n"
                   "/start - Displays this message.\n"
                   "/contact - Displays contact info.\n"
                   "/datetime - Displays current date and time.\n"
                  ) 
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=textMessage)

#/contact sent by user
def contact(update, context):
    textMessage = ("You can contact me via:\n\n"
                   "*Telegram:* @username\n"
                  )
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=textMessage, parse_mode=ParseMode.MARKDOWN_V2)

#/datetime sent by user
def datetime(update, context):
    textMessage = "The datetime\U0000231a now is " + strftime("%Y-%m-%d %H:%M:%S", localtime())
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=textMessage)

#Main
def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('contact',contact))
    dp.add_handler(CommandHandler('datetime',datetime))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
