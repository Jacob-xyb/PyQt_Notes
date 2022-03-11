# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        # Form = QWidget()
        # Form.resize(400, 300)
        Form.setWindowTitle("QLabel_Func")
        self.LbName1 = QLabel(Form)
        self.LbName1.setText("&Name")
        self.EdName1 = QLineEdit(Form)
        self.LbName1.setBuddy(self.EdName1)
        self.LbName2 = QLabel(Form)
        self.LbName2.setText("&Password")
        self.EdName2 = QLineEdit(Form)
        self.LbName2.setBuddy(self.EdName2)
        self.BtnOK = QPushButton(Form)
        self.BtnOK.setText("&OK")
        self.BtnCancel = QPushButton(Form)
        self.BtnCancel.setText("&Cancel")
        mainLayout = QGridLayout(Form)
        mainLayout.addWidget(self.LbName1, 0, 0)
        mainLayout.addWidget(self.EdName1, 0, 1, 1, 2)
        mainLayout.addWidget(self.LbName2, 1, 0)
        mainLayout.addWidget(self.EdName2, 1, 1, 1, 2)
        mainLayout.addWidget(self.BtnOK, 2, 1)
        mainLayout.addWidget(self.BtnCancel, 2, 2)


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
