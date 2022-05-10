"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 14:16"
"""

"""
Example：
创建一个窗口，包含十个标签。
利用父类实现：点击哪个标签就改变哪个标签的背景颜色。
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example5")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # 先创建好一个标签对象
        for i in range(1, 11):
            label = QLabel(self)
            label.resize(100, 20)
            label.setAlignment(Qt.AlignCenter)
            label.move(40 * i, 20 * i)
            label.setText(f"标签 {i}")

    def mousePressEvent(self, e: QMouseEvent) -> None:
        tempWidget = self.childAt(e.localPos().toPoint())
        if tempWidget:
            tempWidget.setStyleSheet("background-color: red;")
        return super(Window, self).mousePressEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


