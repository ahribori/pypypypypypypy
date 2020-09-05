import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우
        self.setWindowTitle("가즈아!")
        self.setGeometry(300, 300, 300, 400)

        # 버튼
        button1 = QPushButton("클릭", self)
        button1.move(20, 20)
        button1.clicked.connect(self.on_button1_clicked)

    def on_button1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
