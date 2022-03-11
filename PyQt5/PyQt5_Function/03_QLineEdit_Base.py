# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap, QIntValidator, QDoubleValidator


class Ui_Form(object):
    def setupUi(self, Form):
        flo = QFormLayout(Form)
        self.LEdit_Normal = QLineEdit(Form)
        self.LEdit_NoEcho = QLineEdit(Form)
        self.LEdit_Password = QLineEdit(Form)
        self.LEdit_PasswordEcho = QLineEdit(Form)
        # 验证器
        # 验证器 - int
        Validator_Int = QIntValidator(self)
        Validator_Int.setRange(0, 9)
        # 验证器 - double
        Validator_Double = QDoubleValidator(self)
        Validator_Double.setRange(-360., 360.)  # 有bug
        Validator_Double.setTop(360)
        Validator_Double.setNotation(QDoubleValidator.StandardNotation)  # 不设置就会超出范围
        Validator_Double.setDecimals(2)  # 不设置就不能填小数
        self.LEdit_Validator = QLineEdit(Form)
        self.LEdit_Validator.setValidator(Validator_Double)

        flo.addRow("Normal", self.LEdit_Normal)  # 创建一个label
        flo.addRow("NoEcho", self.LEdit_NoEcho)
        flo.addRow("Password", self.LEdit_Password)
        flo.addRow("PasswordEcho", self.LEdit_PasswordEcho)
        flo.addRow("验证器", self.LEdit_Validator)

        self.LEdit_Normal.setPlaceholderText("Normal")  # 设置默认输入提示
        self.LEdit_NoEcho.setPlaceholderText("NoEcho")
        self.LEdit_Password.setPlaceholderText("Password")
        self.LEdit_PasswordEcho.setPlaceholderText("PasswordEcho")
        self.LEdit_Validator.setPlaceholderText("验证器")

        # 设置显示效果
        self.LEdit_Normal.setEchoMode(QLineEdit.Normal)  # 正常显示所输入的字符，此为默认选项
        self.LEdit_NoEcho.setEchoMode(QLineEdit.NoEcho)  # 不显示任何输入的字符，常用于密码类型的输入，且保密密码长度
        self.LEdit_Password.setEchoMode(QLineEdit.Password)  # 显示与平台相关的密码掩码字符，而不是实际输入的字符
        self.LEdit_PasswordEcho.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 在编辑时显示字符，负责显示密码类型的输入
        Form.setLayout(flo)


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
