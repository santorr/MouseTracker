from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolButton


class ToolButton(QToolButton):
    def __init__(self, text="Button", icon=None, tooltip=None):
        QToolButton.__init__(self)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # self.setPopupMode(self.MenuButtonPopup)
        self.setIconSize(QSize(50, 50))
        self.setMinimumSize(QSize(75, 75))
        self.setMaximumSize(QSize(1000, 1000))
        self.setToolTip(tooltip)

        self.tooltip = tooltip
        self.text = text
        self.icon = icon

        self.change_tooltip(self.tooltip)
        self.change_icon(self.icon)
        self.change_text(self.text)

    def change_icon(self,  icon=""):
        icon = QIcon(icon)
        self.setIcon(icon)

    def change_text(self, new_text="Text"):
        self.text = new_text
        self.setText(self.text)

    def change_tooltip(self, new_tooltip=""):
        self.tooltip = new_tooltip
        self.setToolTip(self.tooltip)
