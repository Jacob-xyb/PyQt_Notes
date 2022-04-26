import sys
from untitled import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 比较固定的初始化调用方式


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())



