import flet as ft

class VideoView:
    def __init__(self, controller):
        self.controller = controller
        self.out_txt = ft.Text()
        self.download_btn = ft.ElevatedButton(text="Скачать видео", on_click=self.on_download)
        self.input_link = ft.TextField(label="Вставьте ссылку из YouTube", width=400)

        self.progress_bar = ft.ProgressBar(
            width=400,
            value=0,
            bar_height=10,
            border_radius=5,
            visible=False
        )
        self.percent_text = ft.Text("0%", visible=False)

    def build(self, page: ft.Page):
        page.title = "Download view by link v0.2.0"
        page.theme_mode = ft.ThemeMode.LIGHT

        # Layout
        page.add(
            ft.Row([ft.Text(page.title)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self.input_link, self.download_btn]),
            ft.Row([self.progress_bar]),
            ft.Row([self.percent_text]),
            ft.Row([self.out_txt])
        )

    def on_download(self, e):
        url = self.input_link.value

        self.progress_bar.visible = True
        self.percent_text.visible = True

        self.percent_text.value = "0%"
        self.progress_bar.value = 0

        self.progress_bar.update()
        self.percent_text.update()

        self.controller.start_download(url)

    def update_status(self, message):
        self.out_txt.value = message
        self.out_txt.update()

    def update_progress(self, downloaded_bytes, total_bytes, filename):
        progress = 0

        if total_bytes:
            progress = downloaded_bytes / total_bytes

        self.progress_bar.value = progress
        self.percent_text.value = f"{int(progress * 100)}%"
        self.out_txt.value = f"Загрузка {filename}"

        self.progress_bar.update()
        self.percent_text.update()
        self.out_txt.update()

        if progress >= 1:
            self.progress_bar.visible = False
            self.percent_text.visible = False
            self.out_txt.value = "✅ Загрузка завершена"

            self.progress_bar.update()
            self.percent_text.update()
            self.out_txt.update()
