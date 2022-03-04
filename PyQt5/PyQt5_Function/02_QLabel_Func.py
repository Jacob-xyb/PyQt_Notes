# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtGui import QPalette, QPixmap


class Ui_Form(object):
    def setupUi(self, Form):
        # Form = QWidget()
        Form.setWindowTitle("QLabel_Func")


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)      # 比较固定的初始化调用方式


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
