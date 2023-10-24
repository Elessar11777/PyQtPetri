from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtCore import QSize, Qt

class TopInputWidget(QWidget):
    def __init__(self):
        super(TopInputWidget, self).__init__()
        self.initUI()

    def initUI(self):
        hlayout = QHBoxLayout()
        self.setLayout(hlayout)

        start_button = QPushButton("Начать трансляцию")
        start_button.setMaximumSize(250, 50)
        hlayout.addWidget(start_button)

        # self.setMinimumSize(150, 50)
        # self.setMaximumSize(250, 50)

        hlayout.addStretch()

        code_label = QLabel("Код:")
        hlayout.addWidget(code_label)

        input_field = QLineEdit("Что-нибудь вводите")
        input_field.setMinimumSize(QSize(100, 30))
        input_field.setMaximumSize(QSize(200, 30))
        hlayout.addWidget(input_field)

        hlayout.addStretch()

        rudimentary_button = QPushButton("Закончить трансляцию")
        rudimentary_button.setMaximumSize(250, 50)
        hlayout.addWidget(rudimentary_button)
