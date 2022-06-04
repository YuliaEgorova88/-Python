from telegram import Updater, CommandHandler, CallbackContext
from bots_commands import *

# updater = Updater("5385481257:AAFc-LQ71nlr5SKDFPP0t80PyJ-vqypmeGM")

from telegram.ext import Updater

TOKEN = '5385481257:AAFc-LQ71nlr5SKDFPP0t80PyJ-vqypmeGM'

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))
updater.dispatcher.add_handler(CommandHandler("download", download_video))
updater.dispatcher.add_handler(CommandHandler("getWeather", main))
print('Server started')
updater.start_polling()
updater.idle()
