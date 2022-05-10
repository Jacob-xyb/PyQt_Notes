"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 10:53"
"""

"""
Example：
创建一个窗口，包含一个标签，标签随鼠标位置移动，鼠标设置为指定图标
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example3")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # 先创建好一个标签对象
        self.label = QLabel(self)
        self.label.resize(60, 20)
        self.label.setText("Hello Jx")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: red")
        # 再把鼠标设置一下
        cursor = QCursor(QPixmap("../Globe.ico").scaled(20, 20), 0, 0)
        self.setCursor(cursor)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        self.label.move(e.x(), e.y())
        return super().mouseMoveEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


