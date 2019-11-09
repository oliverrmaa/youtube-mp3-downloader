from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# Configure youtube_dl library options

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


# If song directory does not exist, create song director 
if not os.path.exists('Songs'):
    os.mkdir('Songs')
    os.chdir('Songs')
else:
    os.chdir('Songs')

# If song download queue list does not exist, create queue list
if not os.path.exists('./queue.txt'):
    open('./queue.txt', 'a').close()
else:
    with open('./queue.txt') as q:
        queue_list = q.readlines()
        
# Download songs in queue 
for song in queue_list:
    with youtube_dl.YoutubeDL(download_options) as ydl:
        ydl.download([song])
