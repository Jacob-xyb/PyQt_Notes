# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)
# == QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口（window）。
w = QWidget()
# == 改变尺寸
# setFixed > resize == setGeometry
# == 改变尺寸 == resize()方法能改变控件的大小，这里的意思是窗口宽 int px，高 int px。
w.resize(300, 200)
# == 改变尺寸 == setFixed..()固定宽度，高度
w.setFixedWidth(400)
w.setFixedHeight(300)
tempQize = QSize(380, 280)
w.setFixedSize(tempQize)    # == w.setFixedSize(int, int)
# == 改变尺寸 == setGeometry()同时改变位置和大小
w.setGeometry(580, 380, 360, 260)

# == 设置图标
w.setWindowIcon(QIcon('..\\..\\image\\Globe.ico'))

# == move()是修改控件位置的的方法。注：屏幕坐标系的原点是屏幕的左上角。
w.move(600, 400)      # 不用好像是居中

# == 窗口添加标题    # 默认为 python
w.setWindowTitle('Hello QWidget')

# == 窗口属性
# == 窗口属性 == 直接调用==geometry()
print(f"w.x(): {w.x()} || w.y(): {w.y()}"
      f" || w.width(): {w.width()} || w.height(): {w.height()}")
# geometry()获得客户区的属性
print(f"w.geometry().x(): {w.geometry().x()} || w.geometry().y(): {w.geometry().y()}"
      f" || w.geometry().width(): {w.geometry().width()} || w.geometry().height(): {w.geometry().height()}")
# framGeometry()获得整个窗口的属性
print(f"w.frameGeometry().x(): {w.frameGeometry().x()} || w.frameGeometry().y(): {w.frameGeometry().y()}"
      f" || w.frameGeometry().width(): {w.frameGeometry().width()} || w.frameGeometry().height(): {w.frameGeometry().height()}")
# -------- 并没有觉得有什么区别
# == 窗口属性 == 获得客户区的大小
print(f"w.size() -> QSize: {w.size()}")
# == 窗口属性 == 获得窗口默认大小？？
# 可能窗口不显示默认大小，控件才用
# print(f"w.sizeHint(): {w.sizeHint()}")    # 返回的（-1，-1） 其实是（640，480）
# == 窗口属性 == pos()
print(f"左上角坐标：w.pos() -> QPoint: {w.pos()}")

# show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
w.show()
# 最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
# 当调用exit()方法或直接销毁主控件时，主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
sys.exit(app.exec_())
