"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/9 9:42"
"""
from PyQt5.Qt import *
import sys


class App(QApplication):
    def notify(self, receiver, evt) -> bool:
        # 先完成和父类相同的功能后，就可以打印出自己想查询的信息了
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver, evt)
        # 不知道如何分发信号，就交给父类处理，注意要保持和父类同样的返回值
        return super().notify(receiver, evt)


class Btn(QPushButton):
    def event(self, evt) -> bool:
        # 此处不做判断，也会有很多事件打印出来，其中最核心的是绘制事件。
        if evt.type() == QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        print("鼠标被按下了..")
        return super().mousePressEvent(e)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('事件机制')
        self.resize(600, 450)
        self.move(300, 300)
        self.funcList()

    def funcList(self):
        self.func1()

    def func1(self):
        btn = Btn(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.clicked.connect(lambda: print("按钮被点击了"))


if __name__ == '__main__':
    app = App(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())