#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# Tkinter
https://www.cnblogs.com/shwee/p/9427975.html
https://www.runoob.com/python/python-gui-tkinter.html
"""
import sys
# 这里引入了PyQt5.QtWidgets模块，这个模块包含了基本的组件。
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

if __name__ == '__main__':
    # 每个PyQt5应用都必须创建一个应用对象。sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能
    app = QApplication(sys.argv)
    # QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。
    w = QWidget()
    # 在代码中 QWidge 与 QMainWindow 没有太大区别， QMainWindow 是 QWidge 的继承， 方法比较多。
    # w = QMainWindow()
    # resize()方法能改变控件的大小，这里的意思是窗口宽 int px，高 int px。
    w.resize(600, 400)
    # move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置。注：屏幕坐标系的原点是屏幕的左上角。
    w.move(500, 400)
    # 窗口添加标题    # 默认为 python
    w.setWindowTitle('Simple')
    # show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    w.show()
    # 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
    # 当调用exit()方法或直接销毁主控件时，主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
    sys.exit(app.exec_())





