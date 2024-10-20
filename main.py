import yt_dlp
import flet as ft

def download_video(url, progress_callback):
    
    def hook(d):
        if d['status'] == 'downloading':
            progress_callback(d['downloaded_bytes'], d['total_bytes'], d['filename'])
            
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'progress_hooks': [hook],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Download view by link v0.2.0"
    
    out_txt = ft.Text()
    download_btn = ft.ElevatedButton(text="Скачать видео", on_click=lambda e: start_download())
    input_link = ft.TextField(label="Вставте сылку из YouTube", width=400)
    
    def start_download():
        url = input_link.value
        if url:
            out_txt.value = "Загрузка видео..."
            page.update()
            download_video(url, update_progress)
    
    def update_progress(downloaded_bytes, total_bytes, filename):
        if total_bytes > 0:
            percentage = (downloaded_bytes / total_bytes) * 100
            out_txt.value = f"Загрузка {filename}: {downloaded_bytes} из {total_bytes} байт ({percentage:.2f}%)"
            page.update() 
    
    # View
    page.add(
        ft.Row([ft.Text(page.title)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([input_link, download_btn]),
        ft.Row([out_txt])
    )    


ft.app(main)
