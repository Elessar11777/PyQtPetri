from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar
from PyQt6.QtCore import Qt

class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.initMenu()

    def initMenu(self):
        self.addMenu('Главная')
        self.addMenu('Настройки')
