import time
from PyQt5.QtCore import QThread, pyqtSignal
import pyautogui


class Worker(QThread):
    mouse_location = pyqtSignal(tuple)

    def __init__(self, parent=None, index=0):
        super(Worker, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print("Start recording")
        while True:
            # time.sleep(0.01)
            self.mouse_location.emit((pyautogui.position().x, pyautogui.position().y))

    def stop(self):
        self.is_running = False
        print("Stop recording")
        self.terminate()
