"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 13:49"
"""

"""
Example：
创建一个窗口，包含一个标签。
鼠标移动进来时和出去时的文字不一样；
然后能捕捉快捷键：tab, ctrl+s, ctrl+shift+a
"""

import sys
from PyQt5.Qt import *

class Label(QLabel):
    def enterEvent(self, e: QEvent) -> None:
        self.setText("欢迎光临！")
        return super(Label, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        self.setText("谢谢惠顾！")
        return super(Label, self).leaveEvent(e)

    def keyPressEvent(self, ev: QKeyEvent) -> None:
        # 按下单个键
        if ev.key() == Qt.Key_Tab:
            self.setText("按下了 Tab 键")
        # 按下组合键，就要分修饰符和普通键位
        elif ev.modifiers() == Qt.ControlModifier and ev.key() == Qt.Key_S:
            self.setText("按下了 Ctrl+S 键")
        # 如果是多个组合键，用 或| 运算符运算
        elif ev.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and ev.key() == Qt.Key_A:
            self.setText("按下了 Ctrl+Shift+A 键")
        return super(Label, self).keyPressEvent(ev)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example4")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # 先创建好一个标签对象
        self.label = Label(self)
        self.label.resize(100, 80)
        self.label.move(200, 100)
        self.label.setText("Hello Jx")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: red")
        self.label.grabKeyboard()       # 捕获全局键盘


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


