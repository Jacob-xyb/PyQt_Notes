"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/9 15:54"
"""

"""
Example：
通过给定的个数，负责在一个窗口内创建相应个数的子控件。
要求：控件按照九宫格的布局进行摆放。
"""

from PyQt5.Qt import *
import sys

__author__ = "Jacob-xyb"

import sys
from PyQt5.Qt import *


class BaseWidget(QWidget):
    def __init__(self, parent=None, x=10, y=10):
        super().__init__(parent)
        self.resize(x, y)

    def paintEvent(self, event):
        # 以下几行代码的功能是避免在多重传值后的功能失效
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)


class Btn(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example1")
        self.totalCol = 3
        self.setup_ui()

    def setup_ui(self):
        inputNums = 66
        if inputNums % self.totalCol:
            self.totalRow = inputNums // self.totalCol + 1
        else:
            self.totalRow = inputNums // self.totalCol
        # 先设置顶层控件的尺寸
        temp_x, temp_y = 100, 20
        self.resize(self.totalCol * temp_x, self.totalRow * temp_y)
        # 开始添加控件
        for i in range(inputNums):
            temp_qwidget = BaseWidget(self, temp_x, temp_y)
            temp_qwidget.setStyleSheet("background-color: red;border: 1px solid yellow")
            pos_x = (i % self.totalCol) * temp_x
            pos_y = (i // self.totalCol) * temp_y
            temp_qwidget.move(pos_x, pos_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


