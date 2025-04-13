#Lyra Hering u1514295
#Github Repo Name: LyraHering

import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
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
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 21
        self.frames = load_sprite('spriteImages',self.num_frames)
        self.frame_index = 0

        # Add any other instance variables needed to track information as the program
        # runs here
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()
        main_layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setPixmap(self.frames[0])
        main_layout.addWidget(self.image_label)

        fps_layout = QHBoxLayout()
        fps_label = QLabel("Frames per second:")
        fps_layout.addWidget(fps_label)
        self.fps_value = QLabel("30")
        fps_layout.addWidget(self.fps_value)
        main_layout.addLayout(fps_layout)

        self.fps_slider = QSlider(Qt.Orientation.Vertical)
        self.fps_slider.setRange(1, 100)
        self.fps_slider.setValue(30)
        self.fps_slider.setTickInterval(10)
        self.fps_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.fps_slider.valueChanged.connect(self.update_fps_label)
        main_layout.addWidget(self.fps_slider)

        self.start = QPushButton("Start")
        self.start.clicked.connect(self.start_animation)
        main_layout.addWidget(self.start)

        frame.setLayout(main_layout)
        self.setCentralWidget(frame)

        # Add a lot of code here to make layouts, more QFrame or QWidgets, and
        # the other components of the program.
        # Create needed connections between the UI components and slot methods
        # you define in this class.


    # You will need methods in the class to act as slots to connect to signals
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

def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()