from PyQt5.Qt import QApplication, QWidget, QPushButton, qApp, QObject
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.resize(600, 500)
        self.object = QObject(self)
        self.func_list()

    def func_list(self):
        # self.func1()
        # self.func2()
        self.func3()

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
