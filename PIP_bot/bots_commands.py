import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import datetime
from spy import *
from pytube import YouTube

import datetime
from config import open_weather_key
import requests
from pprint import pprint


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


def get_weather(city, open_weather_key):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_key}&units=metric"
        )
        data = r.json()
        # pprint(data)
        weather_Descryption = data["weather"][0]["main"]
        if weather_Descryption in code_to_smile:
            wd = code_to_smile[weather_Descryption]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"

        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        wind_speed = data["wind"]["speed"]
        length_of_the_day = sunset_timestamp - sunrise_timestamp

        print(f'**** {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")} ****'
              f'\nПогода в городе: {city}'
              f'\nТемпаратура: {temp}°С {wd}'
              f'\nВлажность: {humidity}%'
              f'\nДавление: {pressure}-мм.рт.ст'
              f'\nВетер: {wind_speed}-м/с'
              f'\nВосход солнца: {sunrise_timestamp}'
              f'\nЗакат солнца: {sunset_timestamp}'
              f'\nПродолжительность дня: {length_of_the_day}'
              f'\nХорошего дня')

    except Exception as ex:
        print(ex)
        print('Проверьте название города!')


def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_key)


if __name__ == '__main__':
    main()
