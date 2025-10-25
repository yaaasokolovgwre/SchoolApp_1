import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моё первое GUI-приложение")
        self.setGeometry(300, 200, 300, 200)

        self.label = QLabel("Привет, мир!", self)
        self.button = QPushButton("Нажми меня", self)
        self.button.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        self.label.setText("Кнопка нажата!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
