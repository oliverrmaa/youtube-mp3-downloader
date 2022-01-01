# youtube-mp3-downloader

## Introduction:

This repo utilizes the `youtube_dl` library to download songs from youtube in
bulk.

## Installation:

Please install dependencies using:

```
cd youtube-mp3-downloader
pip install -r requirements.txt
```

If you are a mac user, it is possible further dependencies may be needed in
which case, please use `brew install ffmpeg`.

## Instructions:

To utilize this program open the command line and run the following
commands, first `cd youtube-mp3-downloader`.

Then run `python downloader.py open-queue` which will open an empty `queue.txt`
file in your default text editor. This will serve as the interface where you
can add a list of songs to be downloaded. Simply copy and paste the necessary
youtube links in. Please only place one link per line and make sure to not have
any extra spaces on the line.

When you are happy with your `queue.txt` list of songs, run
`python downloader.py run`. This will automatically download the songs to the
`Songs/` directory.

You may specify a different directory (for example `/Users/Downloads/`)
by placing the directory path after `run`:

```
python downloader.py run /Users/oliverma/Downloads/
```

Note that if you use `python downloader.py` without either option, an exception
will be raised.
