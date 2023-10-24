from PyQt6 import QtCore, QtWidgets
from Views.MainWindow import MainWindow
from Styles.Styling import css_style




if __name__ == "__main__":
    # Init App
    app = QtWidgets.QApplication([])
    app.setStyle('fusion')
    app.setStyleSheet(css_style)
    # Widgets Call
    main_window = MainWindow()
    main_window.show()
    #
    app.exec()

