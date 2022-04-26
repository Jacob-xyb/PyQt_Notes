# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QPalette, QPixmap, QIntValidator, QDoubleValidator, QRegExpValidator


class Ui_Form(object):
    def setupUi(self, Form):
        self.layout = QGridLayout()
        self.PushButton_test = QPushButton(Form)
        self.PushButton_test.setText("&Download")
        Form.resize(541, 313)
        self.layout.addWidget(self.PushButton_test)
        Form.setLayout(self.layout)


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 比较固定的初始化调用方式


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
