"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/9 21:07"
"""

"""
Example：
创建一个窗口，包含一个标签，标签内容为：Hello Jx
标签大小为100,60; 将标签文字放置在标签右下角
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example2")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.resize(100, 60)
        self.label.setText("Hello Jx")
        self.label.setStyleSheet("background-color: cyan")
        self.label.setContentsMargins(50, 30, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


