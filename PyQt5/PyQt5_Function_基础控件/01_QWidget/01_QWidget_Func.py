# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QWidget_Func")
        # == 设置气泡提示
        # == 静态方法设置字体
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("这是一个<b>气泡提示</b>")
        # =================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WinForm()
    w.show()
    sys.exit(app.exec_())


