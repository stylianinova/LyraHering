#Lyra Hering u1514295
#Github Repo Name: LyraHering
#Github web address: https://github.com/stylianinova/LyraHering

import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)
        self.frame_index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.setupUI()


    def setupUI(self):
        frame = QFrame()
        main_layout = QVBoxLayout()

        image_and_slider_layout = QHBoxLayout()

        self.image_label = QLabel()
        self.image_label.setPixmap(self.frames[0])
        image_and_slider_layout.addWidget(self.image_label)

        self.fps_slider = QSlider(Qt.Orientation.Vertical)
        self.fps_slider.setRange(1, 100)
        self.fps_slider.setValue(30)
        self.fps_slider.setTickInterval(10)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksLeft)
        self.fps_slider.valueChanged.connect(self.update_fps_label)

        image_and_slider_layout.addWidget(self.fps_slider)
        main_layout.addLayout(image_and_slider_layout)

        fps_label_layout = QHBoxLayout()
        fps_text = QLabel("Frames per second:")
        self.fps_value = QLabel("30")
        fps_label_layout.addWidget(fps_text)
        fps_label_layout.addWidget(self.fps_value)
        main_layout.addLayout(fps_label_layout)

        self.start = QPushButton("Start")
        self.start.clicked.connect(self.start_animation)
        main_layout.addWidget(self.start)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        pause = QAction("Pause", self)
        pause.triggered.connect(self.pause)
        file_menu.addAction(pause)
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(QApplication.quit)
        file_menu.addAction(exit_action)

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

    def update_fps_label(self):
        fps = self.fps_slider.value()
        self.fps_value.setText(str(fps))
        self.timer.setInterval(1000 // fps)

    def update_frame(self):
        self.frame_index = (self.frame_index + 1) % self.num_frames
        self.image_label.setPixmap(self.frames[self.frame_index])

    def start_animation(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start.setText("Start")
        else:
            fps = self.fps_slider.value()
            self.timer.start(1000 // fps)
            self.start.setText("Stop")

    def pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start.setText("Start")

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()