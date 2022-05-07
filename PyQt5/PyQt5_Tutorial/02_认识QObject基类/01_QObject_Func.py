"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/7 20:32"
"""

import time
from PyQt5.Qt import QApplication, QWidget, QPushButton, qApp, QObject, Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.resize(600, 500)
        self.object = QObject(self)
        self.func_list()

    def func_list(self):
        self.func1()

    def func1(self):
        def slotTitle(title):
            self.blockSignals(True)
            self.setWindowTitle("Jx-"+title)
            self.blockSignals(False)

        self.windowTitleChanged.connect(slotTitle)
        self.setWindowTitle("信号与槽案例")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    window = Window()
    window.show()
    sys.exit(app.exec_())  # 0是正常退出
