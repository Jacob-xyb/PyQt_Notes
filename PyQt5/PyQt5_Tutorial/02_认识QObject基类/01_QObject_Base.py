import time

from PyQt5.Qt import QApplication, QWidget, QPushButton, qApp, QObject
import sys


class JxObject(QObject):
    def timerEvent(self, QTimerEvent) -> None:
        print(QTimerEvent, time.time())


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.resize(600, 500)
        self.object = QObject(self)
        self.func_list()

    def func_list(self):
        # self.func1()
        # self.func2()
        # self.func3()
        # self.func4()
        # self.func5()
        # self.func6()
        self.func7()

    def func1(self):
        print(self.object.objectName())     # 初始化时，name为空
        self.object.setObjectName("firstName")
        print(self.object.objectName())

    def func2(self):
        self.object.setProperty('level1', '第一')     # 给对象添加一个属性和值
        tempList = [1, 2, 3, 4, 5]
        self.object.setProperty('level2', tempList)
        print(self.object.property('level1'))       # 获取属性对应的值，没有返回None，相当于字典
        print(self.object.property('level2'))
        print(self.object.dynamicPropertyNames())

    def func3(self):
        object1 = QObject()
        object1.setObjectName("obj1")
        object2 = QObject()
        object2.setObjectName("obj2")
        object3 = QObject()
        object3.setObjectName("obj3")
        object2.setParent(object1)
        object3.setParent(object2)
        print(object1.parent())     # None
        print(object2.parent().objectName())        # obj1
        print(object2.children()[0].objectName())   # obj3
        print(object3.children())   # []

        print(object1.findChild(QObject).objectName())      # obj2
        print(object1.findChildren(QObject))                # 找到了两个对象

    def func4(self):
        print(self.object.isWidgetType())       # False # 判断是否为 Widget
        print(self.object.isWindowType())       # False # 判断是否为 Window
        print(self.object.inherits('QPushButton'))    # False # 判断继承
        btn = QPushButton()
        print(btn.inherits('QObject'))          # True

    def func5(self):
        object1 = QObject()
        object1.setObjectName("obj1")
        object2 = QObject()
        object2.setObjectName("obj2")
        object3 = QObject()
        object3.setObjectName("obj3")
        self.object.destroyed.connect(lambda: print('object被释放'))
        object1.destroyed.connect(lambda: print('object1被释放'))
        object2.destroyed.connect(lambda: print('object2被释放'))
        object3.destroyed.connect(lambda: print('object3被释放'))
        object2.deleteLater()

    def func6(self):
        btn = QPushButton(self)
        self.obj = JxObject()
        startId = self.obj.startTimer(1000)
        btn.pressed.connect(lambda: self.obj.killTimer(startId))

    def func7(self):
        self.object.objectNameChanged.connect(lambda x: print("Name Changed", x))
        btn = QPushButton(self)
        # btn.clicked.connect(lambda: self.object.setObjectName("hello"))   # 这个只会接收一次
        btn.clicked.connect(lambda: self.object.setObjectName(f"{time.time()}"))    # 这个更好玩
        

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    # sys.argv可以接收用户命令行启动时所输入的参数，根据参数执行不同程序
    # qApp 为全局对象
    print(sys.argv)
    print(app.arguments())
    print(qApp.arguments())
    # 以上三个输出结果是一样的
    window = Window()

    window.show()
    sys.exit(app.exec_())  # 0是正常退出
