import ctypes
import sys
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QFileDialog
from Application.worker import Worker
from Application.views.custom_widgets import ToolButton
from Application.controllers.algorithm import AlgorithmPoint


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.recording = False
        self.screen_information = self.get_screen_information()

        self.thread = {}
        self.thread[1] = Worker(parent=None, index=1)
        self.thread[1].mouse_location.connect(self.update_data)

        """ Select an algorithm """
        self.algorithm = AlgorithmPoint(width=self.screen_information.get("width"),
                                        height=self.screen_information.get("height"),
                                        tick=0.01)
        self.data = []

        self.set_style()

    def set_style(self):
        """ Create the style for the application """
        main_widget = QWidget()
        self.horizontal_grid = QHBoxLayout()
        self.setLayout(self.horizontal_grid)
        """ Create the main widget """
        main_widget.setLayout(self.horizontal_grid)
        self.setCentralWidget(main_widget)

        self.btn_record = ToolButton(text="Play", icon="icons/icon_play", tooltip="Record a new sequence")
        self.btn_reset_data = ToolButton(text="Reset", icon="icons/icon_reset")
        self.btn_save = ToolButton(text="Save", icon="icons/icon_save")
        self.btn_exit = ToolButton(text="Exit", icon="icons/icon_exit")

        self.btn_record.clicked.connect(self.record)
        self.btn_reset_data.clicked.connect(self.reset_data)
        self.btn_save.clicked.connect(self.save_texture)
        self.btn_exit.clicked.connect(self.exit_application)

        self.horizontal_grid.addWidget(self.btn_record)
        self.horizontal_grid.addWidget(self.btn_reset_data)
        self.horizontal_grid.addWidget(self.btn_save)
        self.horizontal_grid.addWidget(self.btn_exit)

    def record(self):
        """ Pressed the record button """
        if self.recording:  # Stop the record
            self.thread[1].stop()
            self.recording = False
            self.btn_reset_data.setEnabled(True)
            self.btn_save.setEnabled(True)
            self.btn_record.change_icon("icons/icon_play")
            self.btn_record.change_text("Play")
        else:  # Start the record
            self.thread[1].start()
            self.recording = True
            self.btn_reset_data.setEnabled(False)
            self.btn_save.setEnabled(False)
            self.btn_record.change_icon("icons/icon_stop")
            self.btn_record.change_text("Stop")

    def update_data(self, mouse_location):
        """ Mouse location = (width, height) """
        self.data.append((mouse_location[0], mouse_location[1]))

    def reset_data(self):
        """ Reset all data """
        self.data.clear()

    def save_texture(self):
        """ Save the texture where you want """
        img = self.algorithm.process(self.data)
        complete_path, extension = QFileDialog.getSaveFileName(None, "Save as", "", "Jpg (*.jpg);; Jpeg (*.jpeg)")
        if complete_path:
            img.save(complete_path)

    @staticmethod
    def get_screen_information():
        """ Return the screen size """
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        screen_height = user32.GetSystemMetrics(1)
        screen_width = user32.GetSystemMetrics(0)
        return {"height": screen_height, "width": screen_width}

    def exit_application(self):
        """ Quit the application """
        if self.recording:
            self.recording = False
        sys.exit()
