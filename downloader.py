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


# If song directory does not exist, create song directory
if not os.path.exists('Songs'):
    os.mkdir('Songs')
    os.chdir('Songs')
else:
    os.chdir('Songs')

# If song download queue list does not exist, create queue list
if not os.path.exists('./queue.txt'):
    print("First run, creating empty queue list")
    open('./queue.txt', 'a').close()
    queue_list = list()
else:
    with open('./queue.txt') as q:
        queue_list = q.readlines()

# Download songs in queue
if not len(queue_list)==0:
    for idx, song in enumerate(queue_list):
        print("Now downloading song {} / {}".format(idx+1, len(queue_list)))
        with youtube_dl.YoutubeDL(download_options) as ydl:
            ydl.download([song])
else:
    print("No songs in the queue")

# Clear the queue list for use on the next run
print("Now erasing the queue list for reuse on next run")
q = open('./queue.txt', 'w')
q.close()
