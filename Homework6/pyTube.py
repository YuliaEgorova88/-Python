from pytube import YouTube
from telegram import Update
import telegram.ext
from telegram.ext import Updater, ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("5385481257:AAFc-LQ71nlr5SKDFPP0t80PyJ-vqypmeGM").build()


async def hello(update: Update, context: ContextTypes):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def save_video(update: Update, context: ContextTypes):
    global app
    msg = update.message.text
    print(msg)
    items = msg.split(' ')
    yt = YouTube(items[1])
    yt.streams.filter(progressive=True, file_extension='mp4')
    yt.streams.order_by('resolution')
    yt.streams.desc()
    yt.streams.first().download(output_path=r"/Users/yuliyaskripnik/PycharmProjects/-Python/Homework6/downloaded",
                                filename='my_video.mp4'
                                )
    # video = open(r"/Users/yuliyaskripnik/PycharmProjects/-Python/Homework6/downloaded/yt_video.mp4", 'rb')
    # app.send_video(update.message.chat.id, video)
    await update.message.reply_video(r"/Users/yuliyaskripnik/PycharmProjects/-Python/Homework6/downloaded/my_video.mp4")


# update.message.reply_video(video)

# app.add_handler(CommandHandler(get_link))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("save", save_video))

print('server start')
app.run_polling(stop_signals=None)

import tkinter as tk
from tkinter import Tk, Frame, BOTH

#
# class Example(Frame):
#
#     def __init__(self, parent):
#     Frame.__init__(self, parent, background="white")
#     self.parent = parent
#     self.parent.title("Video_Downloading")
#     self.pack(fill=BOTH, expand=1)
#     self.centerWindow()
#
# def centerWindow(self):
#     w = 390
#     h = 250

#         sw = self.parent.winfo_screenwidth()
#         sh = self.parent.winfo_screenheight()
#
#         x = (sw - w) / 2
#         y = (sh - h) / 2
#         self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
#
#
# def main():
#     root = Tk()
#     ex = Example(root)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()



