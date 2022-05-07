import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


# 我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定
class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        # closeApp信号QMainWindow的close()方法绑定。
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
