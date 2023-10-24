# CenterWidget.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem, QGridLayout
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt
from Views.MainViews.CenterViews.TopInputWidget import TopInputWidget

class CenterWidget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.initGridLayout()

    def initGridLayout(self):
        glayout = QGridLayout()
        self.setLayout(glayout)


        input_widget = TopInputWidget()
        glayout.addWidget(input_widget, 0, 0, 1, 12, alignment=Qt.AlignmentFlag.AlignTop)

        # glayout.addWidget(QPushButton(), 1, 1)

        # current_size = self.size()
        # print(f"Width: {current_size.width()}, Height: {current_size.height()}")
