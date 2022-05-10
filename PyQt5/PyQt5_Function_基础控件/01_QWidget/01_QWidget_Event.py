"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 11:34"
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        pass

    def showEvent(self, e: QShowEvent) -> None:
        print("窗口开始展示，触发showEvent事件")
        return super(Window, self).showEvent(e)

    def closeEvent(self, e: QCloseEvent) -> None:
        print("触发closeEvent事件")
        return super(Window, self).closeEvent(e)

    def moveEvent(self, e: QMoveEvent) -> None:
        print("窗口被移动")  # show() 时就会打印一次
        return super(Window, self).moveEvent(e)

    def resizeEvent(self, e: QResizeEvent) -> None:
        print("窗口改变了尺寸大小")  # show() 时也会触发一次
        return super(Window, self).resizeEvent(e)

    def enterEvent(self, e: QEvent) -> None:
        print("鼠标进来了")
        self.setStyleSheet("background-color: yellow;")
        return super(Window, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        print("鼠标离开了")
        self.setStyleSheet("background-color: red;")
        return super(Window, self).leaveEvent(e)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print("鼠标被按下")
        return super(Window, self).mousePressEvent(e)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        print("鼠标被释放了")
        return super(Window, self).mouseReleaseEvent(e)

    def mouseDoubleClickEvent(self, e: QMouseEvent) -> None:
        print("鼠标双击")
        return super(Window, self).mouseDoubleClickEvent(e)

    def keyPressEvent(self, e: QKeyEvent) -> None:
        print("键盘上某一个按键被按下")
        return super(Window, self).keyPressEvent(e)

    def keyReleaseEvent(self, e: QKeyEvent) -> None:
        print("键盘上某一个按键被释放")
        return super(Window, self).keyReleaseEvent(e)

    # 获取焦点时使用
    def focusInEvent(self, e: QFocusEvent) -> None:
        return super(Window, self).focusInEvent(e)

    # 失去焦点时使用
    def focusOutEvent(self, e: QFocusEvent) -> None:
        return super(Window, self).focusOutEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
