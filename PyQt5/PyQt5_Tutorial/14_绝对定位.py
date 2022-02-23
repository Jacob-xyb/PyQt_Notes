"""
绝对定位
每个程序都是以像素为单位区分元素的位置，衡量元素的大小。所以我们完全可以使用绝对定位搞定每个元素和窗口的位置。但是这也有局限性：
- 元素不会随着我们更改窗口的位置和大小而变化。
- 不能适用于不同的平台和不同分辨率的显示器
- 更改应用字体大小会破坏布局
- 如果我们决定重构这个应用，需要全部计算一下每个元素的位置和大小
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
