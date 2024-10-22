# model.py

import yt_dlp

class VideoDownloader:
    def __init__(self):
        self.filename = ""
        self.downloaded_bytes = 0
        self.total_bytes = 0

    def download_video(self, url, progress_callback):
        def hook(d):
            if d['status'] == 'downloading':
                self.downloaded_bytes = d['downloaded_bytes']
                self.total_bytes = d['total_bytes']
                self.filename = d['filename']
                progress_callback(self.downloaded_bytes, self.total_bytes, self.filename)

        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'progress_hooks': [hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
