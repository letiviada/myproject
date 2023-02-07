#!/usr/local/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)

        self.create_buttons()
        self.layout_widgets()
        self.connect_buttons()

    def create_buttons(self):
        self.buttons = []
        for i in range(10):
            self.buttons.append(QPushButton(str(i)))

        self.add_button = QPushButton("+")
        self.subtract_button = QPushButton("-")
        self.multiply_button = QPushButton("*")
        self.divide_button = QPushButton("/")
        self.equal_button = QPushButton("=")
        self.clear_button = QPushButton("Clear")

    def layout_widgets(self):
        layout = QVBoxLayout()

        layout.addWidget(self.result_display)

        for button in self.buttons:
            layout.addWidget(button)

        layout.addWidget(self.add_button)
        layout.addWidget(self.subtract_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.divide_button)
        layout.addWidget(self.equal_button)
        layout.addWidget(self.clear_button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def connect_buttons(self):
        for button in self.buttons:
            button.clicked.connect(self.append_number)

        self.add_button.clicked.connect(lambda: self.append_operator("+"))
        self.subtract_button.clicked.connect(lambda: self.append_operator("-"))
        self.multiply_button.clicked.connect(lambda: self.append_operator("*"))
        self.divide_button.clicked.connect(lambda: self.append_operator("/"))
        self.equal_button.clicked.connect(self.calculate)
        self.clear_button.clicked.connect(self.clear)

    def append_number(self):
        sender = self.sender()
        self.result_display.setText(self.result_display.text() + sender.text())

    def append_operator(self, operator):
        self.result_display.setText(self.result_display.text() + operator)

    def calculate(self):
        expression = self.result_display.text()
        result = eval(expression)
        self.result_display.setText(str(result))

    def clear(self):
        self.result_display.clear()
        
app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec_())
