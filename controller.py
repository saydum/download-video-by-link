# controller.py

from model import VideoDownloader

class VideoController:
    def __init__(self, view):
        self.view = view
        self.downloader = VideoDownloader()

    def start_download(self, url):
        if url:
            self.view.update_status("Загрузка видео...")
            # Передаем метод обновления прогресса как коллбек
            self.downloader.download_video(url, self.view.update_progress)
