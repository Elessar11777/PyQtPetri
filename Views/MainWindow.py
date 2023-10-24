from PyQt6.QtWidgets import QApplication, QMainWindow
from Views.MainViews.MenuBar import MenuBar
from Views.MainViews.CenterWidget import CenterWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initMenu()
        self.initCenterWidget()


    def initUI(self):
        self.setWindowTitle('Aeya')
        self.setGeometry(300, 300, 1280, 800)  # Set window size and position
        self.center()

    def initMenu(self):
        menubar = MenuBar()
        self.setMenuBar(menubar)

    def initCenterWidget(self):
        center_widget = CenterWidget()
        self.setCentralWidget(center_widget)

        # center_widget.resize(self.width(), self.height())

        # self.setCentralWidget(center_widget)
        # print(self.centralWidget().size())
        # position = self.centralWidget().pos()
        # print("X:", position.x())
        # print("Y:", position.y())


    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
