import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 创建了一个类的调用，这个类继承自QWidget
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 使用继承自QWidget类的方法
        # setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('..\\..\\image\\Globe.ico'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
