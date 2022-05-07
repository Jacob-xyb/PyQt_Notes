import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)
        x = 0
        y = 0
        self.text = "x: {0},  y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        # X Y坐标显示在QLabel组件里
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    # e代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。x()和y()方法得到鼠标的x和y坐标点，然后拼成字符串输出到QLabel组件里。
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())