"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/11 9:52"
"""

"""
Example：
创建一个窗口，无边框无标题栏，窗口半透明，自定义最小化，最大化，关闭按钮，支持拖拽用户区移动
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example6")
        self.dragFlag = False
        self.current_pos = None
        self.current_widget_pos = None
        self.setup_ui()
        self.resize(600, 400)

    def setup_ui(self):
        self.setWindowOpacity(0.5)      # 设置窗口半透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 创建三个子控件按钮
        self.btn_minimum = QPushButton(self)
        self.btn_minimum.setText("最小化")
        self.btn_maximum = QPushButton(self)
        self.btn_maximum.setText("最大化")
        self.btn_close = QPushButton(self)
        self.btn_close.setText("关闭")
        # 如果不手动 resize，就会有问题：第一次调用的 width 与实际的 width 不一致
        self.btn_minimum.resize(75, 25)
        self.btn_maximum.resize(75, 25)
        self.btn_close.resize(75, 25)
        # 设置功能
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_minimum.clicked.connect(lambda: self.showMinimized())
        self.btn_maximum.clicked.connect(lambda: self.btnMaxClickEvent())

    def btnMaxClickEvent(self):
        if self.windowState() == Qt.WindowNoState:
            self.btn_maximum.setText("缩放窗口")
            self.showMaximized()
        else:
            self.btn_maximum.setText("最大化")
            self.showNormal()

    def resizeEvent(self, e: QResizeEvent) -> None:
        # 摆放这些按钮
        width = self.width()
        btn_close_x = width - self.btn_close.width()
        btn_close_y = 10
        self.btn_close.move(btn_close_x, btn_close_y)
        self.btn_maximum.move(btn_close_x - self.btn_maximum.width(), btn_close_y)
        self.btn_minimum.move(self.btn_maximum.x() - self.btn_minimum.width(), btn_close_y)
        return super(Window, self).resizeEvent(e)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.dragFlag = True
            self.current_pos = e.globalPos()
            self.current_widget_pos = self.pos()
        return super(Window, self).mousePressEvent(e)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if self.dragFlag:
            self.move(self.current_widget_pos + (self.cursor().pos() - self.current_pos))
        return super(Window, self).mouseMoveEvent(e)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.dragFlag = False
        return super(Window, self).mouseReleaseEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


