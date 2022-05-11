"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/11 13:45"
"""

"""
Example：
创建一个窗口，包含一个文本框、按钮、标签
默认状态：标签隐藏，文本框和按钮显示，按钮设置为不可用状态
要求：1.当文本框有内容时，让按钮可用，否则不可用
     2.当文本框内容为 Jx 时，点击按钮则显示标签，且文本为登陆成功，否则为失败
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example7")
        self.resize(600, 400)
        # 首先创建所有需要的控件
        self.lineEdit = QLineEdit(self)
        self.btn = QPushButton(self)
        self.label = QLabel(self)
        self.setup_ui()

    def setup_ui(self):
        # 简单调整下布局
        self.lineEdit.resize(200, 25)
        self.lineEdit.move(10, 10)
        self.btn.resize(40, 25)
        self.btn.setText("登陆")
        self.btn.move(self.lineEdit.frameGeometry().topRight() + QPoint(10, 0))
        self.label.resize(100, 25)
        self.label.setStyleSheet("background-color: gray")
        self.label.move(self.lineEdit.frameGeometry().bottomLeft() + QPoint(0, 20))
        self.label.setAlignment(Qt.AlignCenter)
        # 默认状态
        self.label.setVisible(False)    # 标签隐藏
        self.btn.setEnabled(False)      # 按钮不可用
        # 实现要求
        self.lineEdit.textChanged.connect(self.textChangedEvent)
        self.btn.clicked.connect(self.btnClickedEvent)

    def textChangedEvent(self):
        self.btn.setEnabled(bool(self.sender().text()))
        self.label.setVisible(False)

    def btnClickedEvent(self):
        if self.lineEdit.text() == "Jx":
            self.label.setText("登陆成功")
        else:
            self.label.setText("登陆失败")
        self.label.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
