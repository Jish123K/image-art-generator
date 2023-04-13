import base64

import os

import pywhatkit

from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        # Set up the GUI

        self.setWindowTitle("Paint AI")

        self.setGeometry(100, 100, 600, 300)

        self.central_widget = QtWidgets.QWidget()

        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout()

        self.central_widget.setLayout(self.layout)

        # Add a label and line edit for the prompt

        self.prompt_label = QtWidgets.QLabel("Prompt:")

        self.prompt_line_edit = QtWidgets.QLineEdit()

        self.layout.addWidget(self.prompt_label)

        self.layout.addWidget(self.prompt_line_edit)

        # Add a label and combo box for the style

        self.style_label = QtWidgets.QLabel("Style:")

        self.style_combo_box = QtWidgets.QComboBox()

        self.style_combo_box.addItems([

            "default", "paint", "hdr", "polygon", "gouache",

            "realistic", "comic", "line-art", "malevolent", "meme",

            "throwback", "ghibli", "melancholic", "provenance", "darkfantasy",

            "fantasy", "mystical", "hd", "synthwave", "vibrant", "blacklight"

        ])

        self.layout.addWidget(self.style_label)

        self.layout.addWidget(self.style_combo_box)

        # Add buttons for generating the image and downloading it

        self.generate_button = QtWidgets.QPushButton("Generate")

        self.generate_button.clicked.connect(self.generate_image)

        self.download_button = QtWidgets.QPushButton("Download")

        self.download_button.clicked.connect(self.download_image)

        self.layout.addWidget(self.generate_button)

        self.layout.addWidget(self.download_button)

        # Store the generated image as an instance variable

        self.generated_image = None

    def generate_image(self):

        # Get the prompt and style from the user input

        prompt = self.prompt_line_edit.text()

        style = self.style_combo_box.currentText()

        # Generate the image using the pywhatkit library

        self.generated_image = pywhatkit.image_to_ascii_art(prompt, "paint", style)

        # Display the generated image in a label

        image_bytes = base64.b64decode(self.generated_image.split(",")[1])

        image_data = QtCore.QByteArray(image_bytes)

        image = QtGui.QImage.fromData(image_data)

        self.image_label = QtWidgets.QLabel()

        self.image_label.setPixmap(QtGui.QPixmap.fromImage(image))

        self.layout.addWidget(self.image_label)

    def download_image(self):

        if self.generated_image:

            # Get the filename from the user

            filename, _ = QtWidgets.QFileDialog.getSaveFileName(

                self, "Save Image", "", "Image Files (*.png *.jpg *.bmp)")

            if filename:

                # Save the generated image to the specified file

                with open(filename, "wb") as f:

                    f.write(base64.b64decode(self.generated_image.split(",")[1]))

if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    main_window = MainWindow()

    main_window.show()

    app.exec_()

