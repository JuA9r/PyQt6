"""

    PyQt calculator program

"""

# import sys
import sys

# import PyQt6
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLineEdit)

from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.textbox = None
        self.setWindowTitle("calculator")
        self.setGeometry(100, 100, 320, 400)
        self.textbox_ui()

    def enter_Push(self):
        print(self.textbox.text())

    def textbox_ui(self):
        self.textbox = QLineEdit("", self)
        self.textbox.setGeometry(0, 0, 320, 30)
        self.textbox.setStyleSheet(

            "color: white;"
            "background-color: black;"
            "font-family: kaiti SC;"
            "font-size: 20px;"

        )
        self.textbox.returnPressed.connect(self.enter_Push)
        # print(self.textbox)


if __name__ == "__main__":
    PyQt_app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    PyQt_app.exec()