import time

from PyQt5.Qt import QApplication, QWidget, QPushButton, qApp, QObject, Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.resize(600, 500)
        self.object = QObject(self)
        self.func_list()

    def func_list(self):
        self.func1()

    def func1(self):
        object0 = QObject()
        object1 = QObject()
        object1.setObjectName("obj1")
        object2 = QObject()
        object2.setObjectName("obj2")
        object3 = QObject()
        object3.setObjectName("obj3")
        object4 = QObject()
        object4.setObjectName("obj4")
        object5 = QObject()
        object5.setObjectName("obj5")
        object6 = QObject()
        object6.setObjectName("obj6")

        object1.setParent(object0)
        object2.setParent(object0)
        object3.setParent(object1)
        object4.setParent(object1)
        object5.setParent(object2)
        object6.setParent(object2)
        print(object0.findChild(QObject, "obj4").objectName())      # obj4
        print(object0.findChild(QObject, "obj4", Qt.FindChildrenRecursively).objectName())  # obj4
        print(object0.findChild(QObject, "obj4", Qt.FindDirectChildrenOnly))    # None



if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    window = Window()
    window.show()
    sys.exit(app.exec_())  # 0是正常退出
