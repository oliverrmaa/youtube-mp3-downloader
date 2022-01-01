# youtube-mp3-downloader

## Introduction:

This repo contains a simple script wrapping around the `youtube_dl` library
making it an easy to use command line interface tool to download songs from
youtube in bulk. 

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

- Run the following which will open an empty `queue.txt` file in your 
default text editor. 

  ```
  python downloader.py open-queue
  ```

- This will serve as the interface where you can add a list of songs to 
be downloaded. Simply copy and paste the necessary youtube links in. 
Please only place one link per line and make sure to not have any extra 
spaces on the line.

- When you are happy with your `queue.txt` list of songs, run the 
following to automatically download the songs to the
`Songs/` directory.

  ```
  python downloader.py run
  ```

- You may specify a different directory (for example `/Users/Downloads/`)
by placing the directory path after `run`.

  ```
  python downloader.py run /Users/Downloads/
  ```

Note that if you use `python downloader.py` without either option, an exception
will be raised.
