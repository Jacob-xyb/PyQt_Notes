import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
# QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        # self.resize(self.sizeHint())
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 得到了主窗口的大小。
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        # 然后把自己窗口的中心点放置到cp -> 也就是屏幕中心。
        qr.moveCenter(cp)
        # 然后把窗口的坐上角的坐标设置为qr的矩形左上角的坐标，这样就把窗口居中了。
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
