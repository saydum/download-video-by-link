# main.py

from view import VideoView
from controller import VideoController
import flet as ft

def main(page: ft.Page):
    view = VideoView(VideoController)  # Исправить, чтобы передать экземпляр
    controller = VideoController(view)
    view.controller = controller
    view.build(page)  # Передаем объект page в метод build

ft.app(main)
