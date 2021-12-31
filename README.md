# youtube-mp3-downloader

This repo utilizes the `youtube_dl` library to download songs from youtube in
bulk. Please install dependencies using:

```
cd youtube-mp3-downloader
pip install -r requirements.txt
```

To utilize this program open the command line and run the following
commands:

```
cd youtube-mp3-downloader
python downloader.py
```

The first run will create the necessary `Songs` directory and subsequent
downloaded songs will be placed here. To add a list of songs to be downloaded,
simply go to the newly created `queue.txt` file and paste the necessary youtube
links in. Please only place one link per line and make sure to not have any
extra spaces on the line.

IF you are a mac user, it is possible further dependencies may be needed in
which case, please use `brew install ffmpeg`.
