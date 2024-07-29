"""

    PyQt calculator program

"""

# import sys
import sys

# import math
import math

# import PyQt6
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLineEdit)

from PyQt6.QtCore import Qt


class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.button = None
        self.textbox = None

        self.setWindowTitle("calculator")
        self.setGeometry(100, 100, 320, 400)
        self.textbox_ui()
        self.make_button()

    def enter_Push(self) -> None:
        print(self.textbox.text())

    def textbox_ui(self) -> None:
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

    def make_button(self) -> None:
        self.button = QPushButton("button", self)
        self.button.setGeometry(0, 30, 80, 80)
        print()


if __name__ == "__main__":
    PyQt_app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    PyQt_app.exec()