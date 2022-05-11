"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 10:28"
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        # == 改变尺寸
        # setFixed > resize == setGeometry
        # == 改变尺寸 == resize()方法能改变控件的大小，这里的意思是窗口宽 int px，高 int px。
        self.move(600, 300)
        self.resize(600, 400)
        self.setup_ui()

    def paintEvent(self, event):
        # 以下几行代码的功能是避免在多重传值后的功能失效
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        print("鼠标移动了")
        return super().mouseMoveEvent(a0)

    def setup_ui(self):
        self.funcList()

    def funcList(self):
        pass


# 获取坐标
def testFunc1(q: QWidget):
    print(f"包含框架的坐标：{q.x(), q.y(), q.pos()}")
    print(f"包含框架的宽和高：{q.frameGeometry().width(), q.frameGeometry().height(), q.frameSize()}")
    print(f"用户区域的坐标：{q.geometry().x(), q.geometry().y(), q.geometry(), q.size(), q.rect()}")
    print(f"用户区域的宽和高：{q.width(), q.height()}")


# 设置坐标
def testFunc2(q: QWidget):
    q.resize(100, 100)
    q.setGeometry(100, 100, 400, 400)   # 用户区域
    q.adjustSize()  # 根据内容自适应大小
    q.setFixedSize(200, 200)    # 固定尺寸


# 设置最大最小尺寸
def testFunc3(q: QWidget):
    print(f"获取最小尺寸的宽度：{q.minimumWidth()}\n"
          f"获取最小尺寸的高度：{q.minimumHeight()}\n"
          f"获取最小尺寸：{q.minimumSize()}\n"
          f"获取最大尺寸：{q.maximumSize()}")
    # 设置
    q.setMinimumSize(10, 10)
    q.setMaximumSize(200, 100)


# 设置内容边距
def testFunc4(q: QWidget):
    q.setStyleSheet("background-color: cyan;")
    print(f"查看内容区域尺寸：{q.contentsRect()}")
    q.setContentsMargins(50, 40, 200, 200)
    print(f"查看内容区域尺寸：{q.contentsRect()}")


# 设置鼠标形状
def testFunc5(q: QWidget):
    q.setCursor(Qt.BusyCursor)
    # 自定义鼠标形状
    pixmap = QPixmap("../Globe.ico")
    pixmap = pixmap.scaled(20, 20)  # 缩放尺寸
    cursor = QCursor(pixmap, 0, 0)
    q.setCursor(cursor)
    q.unsetCursor()     # 重置鼠标
    current_cursor = q.cursor()
    btn = QPushButton(q)
    btn.clicked.connect(lambda: print(current_cursor.pos()))
    print(q.hasMouseTracking())     # 默认是 False
    q.setMouseTracking(True)            # 设置为跟踪状态


# 信息提示
def testFunc6(q: QWidget):
    q.setToolTip("信息提示")
    q.setToolTipDuration(2000)
    q.setWhatsThis("这是个测试")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # == QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。
    window = Window()
    # testFunc5(window)
    testFunc6(window)
    window.show()
    # testFunc2(window)
    # testFunc1(window)
    # testFunc3(window)
    # testFunc4(window)
    sys.exit(app.exec_())
