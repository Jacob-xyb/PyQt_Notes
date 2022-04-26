from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtCore import QSize
# from PyQt5.QtGui import QIcon

import sys


class Ui_Form(object):
    def setupUi(self, Form):
        pass


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