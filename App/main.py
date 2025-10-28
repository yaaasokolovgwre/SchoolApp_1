import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import os

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Сохранение данных")
        self.setGeometry(300, 200, 300, 150)

        self.label = QLabel("Введите значение:")
        self.input = QLineEdit()
        self.save_button = QPushButton("Сохранить")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

        self.save_button.clicked.connect(self.save_data)

        self.load_data()

    def save_data(self):
        value = self.input.text()
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write(value)

    def load_data(self):
        if os.path.exists("data.txt"):
            with open("data.txt", "r", encoding="utf-8") as f:
                value = f.read().strip()
                self.input.setText(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
