from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bots_commands import *
updater = Updater("5385481257:AAFc-LQ71nlr5SKDFPP0t80PyJ-vqypmeGM")

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
updater.dispatcher.add_handler(CommandHandler("download", download_video))
print('Server started')
updater.start_polling()
updater.idle()

