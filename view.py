# view.py

import flet as ft

class VideoView:
    def __init__(self, controller):
        self.controller = controller
        self.out_txt = ft.Text()
        self.download_btn = ft.ElevatedButton(text="Скачать видео", on_click=self.on_download)
        self.input_link = ft.TextField(label="Вставьте ссылку из YouTube", width=400)

    def build(self, page: ft.Page):
        page.title = "Download view by link v0.2.0"
        page.theme_mode = ft.ThemeMode.LIGHT

        # Layout
        page.add(
            ft.Row([ft.Text(page.title)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.input_link, self.download_btn]),
            ft.Row([self.out_txt])
        )

    def on_download(self, e):
        url = self.input_link.value
        self.controller.start_download(url)

    def update_status(self, message):
        self.out_txt.value = message
        self.out_txt.update()  # Обновляем только текстовый элемент

    def update_progress(self, downloaded_bytes, total_bytes, filename):
        if total_bytes > 0:
            percentage = (downloaded_bytes / total_bytes) * 100
            self.out_txt.value = f"Загрузка {filename}: {downloaded_bytes} из {total_bytes} байт ({percentage:.2f}%)"
            self.out_txt.update()  # Обновляем только текстовый элемент
