import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("가즈아!")
        self.setGeometry(300, 300, 300, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = MyWindow()
    my_window.show()
    app.exec_()
