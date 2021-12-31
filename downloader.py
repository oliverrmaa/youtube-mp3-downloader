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

def create_songs_dir(songs_dir):
    """Creates the songs directory if it does not exist already."""
    # If song directory does not exist, create song directory
    if not os.path.exists(songs_dir):
        os.mkdir(songs_dir)
        os.chdir(songs_dir)
    else:
        os.chdir(songs_dir)

def create_queue(queue_list_path):
    """
    Generate queue_list with songs or creates queue.txt in songs directory if
    it does not exist already.
    """
    # If song download queue list does not exist, create queue list
    if not os.path.exists(queue_list_path):
        print("First run, creating empty queue list")
        open(queue_list_path, 'a').close()
        queue_list = list()
    else:
        with open(queue_list_path) as q:
            queue_list = q.readlines()

    return (queue_list)

def open_queue(queue_list_path):
    """Opens a queue .txt file for the user"""
    os.system("open " + queue_list_path)

def download_songs(queue_list, download_options=download_options):
    """Takes in a queue_list as input and downloads each song on the list."""
    # Download songs in queue
    if not len(queue_list)==0:
        for idx, song in enumerate(queue_list):
            print("Now downloading song {} / {}".format(idx+1, len(queue_list)))
            with youtube_dl.YoutubeDL(download_options) as ydl:
                ydl.download([song])
    else:
        print("No songs in the queue")


if __name__ == '__main__':

    # Create necessary paths
    cwd = os.getcwd()
    songs_dir = cwd + '/Songs/'
    queue_list_path = cwd + '/queue.txt'

    if argv[1] == "open-queue":
        open_queue(queue_list_path)
    else:
        # Run functions
        create_songs_dir(songs_dir)
        queue_list = create_queue(queue_list_path)
        download_songs(queue_list)
        # Clear the queue list for use on the next run
        print("Now erasing the queue list for reuse on next run")
        q = open(queue_list_path, 'w')
        q.close()

    # Return to the starting directory
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
