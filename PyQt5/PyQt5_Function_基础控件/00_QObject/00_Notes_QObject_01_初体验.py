"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/8/7 17:41"
"""

from PyQt5.Qt import *
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject")  # 设置标题栏
        self.resize(500, 500)  # 设置尺寸
        self.setup_ui()

    def setup_ui(self):
        # self.QObject_mro()
        # self.QObject_ObjectName()
        self.QObject_property()

    def QObject_mro(self):
        mros = QObject.mro()    # Return a type's method resolution order.
        for mro in mros:
            print(mro)

    def QObject_ObjectName(self):
        obj = QObject()
        print(f"初始化的QObject：{obj.objectName()}")    # ""
        obj.setObjectName('first name')
        print(f"设置后的QObject：{obj.objectName()}")    # "first name"

    def QObject_property(self):
        obj = QObject()
        print(f"{obj.property('jx')}, type: {type(obj.property('jx'))}")    # None, type: <class 'NoneType'>
        obj.setProperty('level1', '第一')     # 给对象添加一个属性和值
        print(f"{obj.property('level1')}, type: {type(obj.property('level1'))}")    # 第一, type: <class 'str'>
        tempList = [1, 2, 3, 4, 5]
        obj.setProperty('level2', tempList)
        print(f"{obj.property('level2')}, "
              f"type: {type(obj.property('level2'))}")    # [1, 2, 3, 4, 5], type: <class 'list'>
        print(f"{obj.dynamicPropertyNames()}")      # return: List[QByteArray]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window.show()
    # sys.exit(app.exec_())       # 开始执行一个应用程序，并进入消息循环
