import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
# 导入designer工具生成的login模块
from MainWin2 import Ui_MainWin


class MyMainForm(QWidget, Ui_MainWin):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)      # 比较固定的初始化调用方式
        x = QPushButton()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())

