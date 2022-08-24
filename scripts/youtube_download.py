from __future__ import unicode_literals
import youtube_dl

def youtube_download(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([str(url)])
        
url = input("Input URL:\n")
youtube_download(url)