import requests  # weather
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
# from telegram import bot

import datetime
from spy import *
from pytube import YouTube


def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hi, beauty {update.effective_user.first_name}!')


def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/download')


def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x + y}')


def download_video(update: Update, context: CallbackContext):
    log(update, context)
    # msg = update.message.text
    # print(msg)
    # items = msg.split(' ')
    # update.message.reply_text()

    yt = YouTube(input('Введите адрес YouTube файла для скачивания: '))
    # "https://www.youtube.com/watch?v=uNYKkrf_0K4"
    path = input('Куда скачиваем файл? ')  # 'downloaded'
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(path)
    # video = open(path, 'rb')
    # update.message.reply_video(video)
