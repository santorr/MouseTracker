import time
from PyQt5.QtCore import QThread, pyqtSignal
import pyautogui


class Worker(QThread):
    mouse_location = pyqtSignal(tuple)

    def __init__(self, parent=None, index=0, tick=0.02):
        super(Worker, self).__init__(parent)
        self.index = index
        self.is_running = True
        self.tick = self.set_tick(tick)

    def run(self):
        """ Start recording """
        while True:
            time.sleep(self.tick)
            self.mouse_location.emit((pyautogui.position().x, pyautogui.position().y))

    def stop(self):
        """ Stop recording """
        self.is_running = False
        print("Stop recording")
        self.terminate()

    def set_tick(self, new_tick):
        """ Set a new tick value """
        if new_tick == 0:
            self.tick = 0.01
        elif new_tick < 0:
            self.tick = abs(new_tick)
        else:
            self.tick = new_tick
