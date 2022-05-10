"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 14:16"
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
        self.setWindowTitle("01_QWidget_Example5")
        self.current_pos = None
        self.current_widget_pos = None
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowOpacity(0.5)      # 设置窗口半透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 创建三个子控件按钮
        btn_minimum = QPushButton(self)
        btn_minimum.setText("最小化")
        btn_maximum = QPushButton(self)
        btn_maximum.setText("最大化")
        btn_close = QPushButton(self)
        btn_close.setText("关闭")
        # 摆放这些按钮
        width = self.width()
        btn_close_x = width - btn_close.width()
        btn_close_y = 10
        btn_close.move(btn_close_x, btn_close_y)


    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.current_pos = e.globalPos()
        self.current_widget_pos = self.pos()
        return super(Window, self).mousePressEvent(e)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if self.current_pos:
            self.move(self.current_widget_pos + (self.cursor().pos() - self.current_pos))
        return super(Window, self).mouseMoveEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


