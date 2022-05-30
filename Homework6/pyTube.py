import pytube
from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=GnxaU0Ut8FQ&t=57s').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=GnxaU0Ut8FQ&t=57s')
path = 'downloaded'
yt.streams.filter(progressive=True, file_extension='mp4')
yt.streams.order_by('resolution')
yt.streams.desc()
yt.streams.first()
yt.streams.first().download(path)