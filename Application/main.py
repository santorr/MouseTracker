import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from views.main_window_style import MainWindow

if __name__ == "__main__":
    """ Run the application """
    app = QApplication(sys.argv)
    app.setApplicationName('Mouse tracker')
    app.setApplicationVersion("0.0.1")
    icon = QIcon("icons/icon_application.ico")
    app.setWindowIcon(icon)
    """ Create the main window """
    window = MainWindow()
    window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    window.setBaseSize(250, 75)
    window.setWindowTitle(" ".join([app.applicationName(), app.applicationVersion()]))
    window.show()
    app.exec_()
