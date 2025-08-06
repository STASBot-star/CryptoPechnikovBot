from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Привет! Бот работает 💸")

def help_command(update, context):
    update.message.reply_text("Я бот для сигналов. Пока что умею только /start")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()