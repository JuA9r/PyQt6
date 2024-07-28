"""

    calculator program

"""

# import sys
import sys

# import PyQt6
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calculator")
        button = QPushButton("button", self)
        button.setGeometry(25, 25, 150, 100)
        self.setGeometry(100, 100, 200, 150)

PyQt_app = QApplication(sys.argv)
calc = Calculator()
calc.show()
PyQt_app.exec()