# PyQt5 安装与配置

## 安装

- 在线安装

  ```python
  pip install PyQt5 -i https://pypi.douban.com/simple
  pip install pyqt5-stubs -i https://pypi.douban.com/simple
  pip install pyqt5-tools -i https://pypi.douban.com/simple
  ```

- 离线安装

  - 不带Designer版

  ```python
  # 提前下载所需安装包
  pip download PyQt5 -i https://pypi.douban.com/simple
  pip download pyqt5-stubs -i https://pypi.douban.com/simple
      
  # requirements.txt 大致内容
  PyQt5_Qt5-5.15.2-py3-none-win_amd64.whl
  PyQt5_sip-12.9.1-cp38-cp38-win_amd64.whl
  PyQt5-5.15.6-cp36-abi3-win_amd64.whl
  
  # 批量安装离线包
  pip install --no-index -r .\requirements.txt
  ```

  - 带Designer版

  ```python
  # 提前安装下载所需安装包
  pip download PyQt5 -i https://pypi.douban.com/simple
  pip download pyqt5-stubs -i https://pypi.douban.com/simple
  pip download pyqt5-tools -i https://pypi.douban.com/simple
  
  # 处理包的版本冲突(尽量跟随Designer的伴随包)
  #	如果没有冲突就直接安装
  
  # requirements.txt 大致内容
  PyQt5_Qt5-5.15.2-py3-none-win_amd64.whl
  PyQt5_sip-12.9.1-cp38-cp38-win_amd64.whl
  pyqt5_tools-5.15.4.3.2-py3-none-any.whl
  pyqt5-5.15.4-cp36.cp37.cp38.cp39-none-win_amd64.whl
  pyqt5_plugins-5.15.4.2.2-cp38-cp38-win_amd64.whl
  python_dotenv-0.19.2-py2.py3-none-any.whl
  qt5_tools-5.15.2.1.2-py3-none-any.whl
  click-7.1.2-py2.py3-none-any.whl
  qt5_applications-5.15.2.2.2-py3-none-win_amd64.whl
  
  # 批量安装离线包
  pip install --no-index -r .\requirements.txt
  ```

## 配置

- step1

  安装好后可以 `win` 搜索 `designer` 查看是否安装成功

- step2

  打开PyCharm，打开File—>Settings—>External Tools,点击加号来添加自己的工具

  ```python
  Name:QtDesigner
  Group:Qt
  Programs:F:\anaconda\Library\bin\designer.exe(这里是各位自己的designer路径，之前所看到的)
  Working directory：$ProjectFileDir$
  ```

- step3

  但是要在PyCharm中把界面的.ui文件转换为.py文件还需要后面的配置。

  重复上述操作，配置pyuic：

  ```python
  Name:Pyuic
  Group:Qt
  Program:F:\anaconda\python.exe(各位自己的python路径)
  Arguments：-m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
  Working directory：$FileDir$
  ```

## 测试

回到PyCharm，Tools—>Qt—>QtDesigner，点击即可打开designer：

然后创建一个最简单的界面，把这个界面保存（默认是保存在当前pycharm项目目录下，我这里命名“first.ui”）

回到pycharm，可以看到工程目录下已经产生了first.ui，右键它，Qt—>Pyuic，点击后即可产生first.py文件，OK接下来就可以愉快地写代码了(⊙o⊙)…

# PyQt5 入门

## 开发模板

```python
from PyQt5.Qt import QApplication, QWidget, QPushButton, qApp
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget中的init方法
        self.setWindowTitle("软件名称")
        self.resize(600, 500)
        self.btn = QPushButton(self)
        self.func_list()

    def func_list(self):
        self.func()

    def func(self):
        self.btn.setText("软件内容")
        self.btn.resize(120, 30)
        self.btn.move(100, 100)
        self.btn.setStyleSheet('background-color:green;font-size:20px;')


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
```

## 最基本的调用方式

- 文件结构

```python
|-- untitled.ui
|
|-- untitled.py
|
|-- UIMain.py
```

- untitled.py

只需要知道此文件中的 UI 类即可，`Ui_Form`

- UIMain.py

```python
import sys
from untitled import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 比较固定的初始化调用方式


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
```

## 分文件调用

https://zhuanlan.zhihu.com/p/95082345?utm_source=com.example.android.notepad

1、使用Qt Designer新建四个不同的ui文件，分别为camerapage.ui、drivepage.ui、mainpage.ui、rangingpage.ui

2、使用pyuic5将四个ui文件转换成对应的py文件，分别为ui_camerapage.py、ui_drivepage.py、ui_mainpage.py、ui_rangingpage.py

3、创建四个“ui_”文件对应的业务逻辑文件，分别为call_camerapage.py、call_drivepage.py、call_mainpage.py、call_rangingpage.py

```python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal,Qt
from HomePages.ui_camerapage import Ui_CameraPage

class CameraPageWindow(QWidget,Ui_CameraPage):
 #声明信号
 	returnSignal = pyqtSignal()

 	def __init__(self,parent=None):
 		super(CameraPageWindow, self).__init__(parent)
 		self.setupUi(self)
 		self.initUI()

 	def initUI(self):
 		self.setLayout(self.gridLayout)

 	self.returnButton.clicked.connect(self.returnSignal)
```

4、这时候需要一个总界面，用来整合所有子页面，并负责界面之间的切换等功能，新建一个mainwindow.py文件，内容如下：

```python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from call_mainpage import MainPageWindow
from call_camerapage import CameraPageWindow
from call_drivepage import DrivePageWindow
from call_rangingpage import RangingPageWindow

class MainWindow(QWidget):
     def __init__(self):
         super().__init__()
         self.initUI()

     def initUI(self):
         self.resize(480,320)
         self.layout = QGridLayout()
         self.setLayout(self.layout)

         self.Stack = QStackedWidget()
         self.layout.addWidget(self.Stack)
         self.mainPageUi = MainPageWindow()
         self.cameraPageUi = CameraPageWindow()
         self.drivePageUi = DrivePageWindow()
         self.rangingPageUi = RangingPageWindow()

         self.Stack.addWidget(self.mainPageUi)
         self.Stack.addWidget(self.cameraPageUi)
         self.Stack.addWidget(self.drivePageUi)
         self.Stack.addWidget(self.rangingPageUi)

         self.mainPageUi.chooseSignal.connect(self.showDialog)

         self.cameraPageUi.returnSignal.connect(self.returnDialog)
         self.drivePageUi.returnSignal.connect(self.returnDialog)
         self.rangingPageUi.returnSignal.connect(self.returnDialog)

     def showDialog(self,msg):
         print(0)
         if msg == 'camera':
         self.Stack.setCurrentIndex(1)
         print(1)
         elif msg == 'ranging':
         self.Stack.setCurrentIndex(2)
         print(2)
         elif msg == 'drive':
         self.Stack.setCurrentIndex(3)
         print(3)

         def returnDialog(self):
         self.Stack.setCurrentIndex(0)
```

这里使用了QStackedWidget叠层窗口，将所有子窗口添加进来，根据不同的点击显示不同的页面。

5、最后，需要有一个main入口，我们单独再写一个main.py文件，这也和C++工程比较统一，具体内容如下：

```python
from PyQt5.QtWidgets import *
from mainwindow import MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
```

# Pydesigner

## 布局管理

### 布局管理入门

![image-20220316110606670](https://s2.loli.net/2022/03/16/bVMxDpENFml32jB.png)

Qt Designer 提供了4种窗口布局方式。

- 垂直布局：控件默认按照从上到下的顺序进行纵向添加。
- 水平布局：控件默认按照从左到右的顺序进行横向添加。
- 栅格布局：将窗口控件放入一个网格之中，然后将它们合理地划分成若干行和列，形成一个个单元。
- 表单布局：控件以两列的形式布局在表单中，其中左列包含标签，右列包含输入控件。

一般布局有两种方式，一是通过布局管理器进行布局；二是通过容器控件进行布局。

### sizePolicy（大小策略）

其实就是对部件大小进行限制的属性

1. sizeHint：QWidget类中的属性

   部件的大小提示，就是指的部件的默认大小，提示的意思是Qt的建议或推荐。

# PyQt5 基础控件描述

## QMainWindow

```python
class QMainWindow(QWidget):
    """ QMainWindow(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
```

- QMainWindow 类中比较重要的方法

|        方法        |                       描述                       |
| :----------------: | :----------------------------------------------: |
|    addToolBar()    |                    添加工具栏                    |
|  centralWidget()   |     返回窗口中心的一个控件，未设置时返回NULL     |
| setCentralWidget() | 设置窗口中心的控件，这个组件或占满所有剩余的区域 |
|     menuBar()      |                返回一个菜单栏对象                |
|    setMenuBar()    |                  设置菜单栏对象                  |
|    statusBar()     |      返回一个状态栏对象,同时开启状态栏显示       |
|   setStatusBar()   |                    设置状态栏                    |

> 注意：QMainWindow不能设置布局（使用setLayout()方法)，因为它有自己的布局。

### 创建主窗口

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


# 创建了一个类的调用，这个类继承自QWidget
class Example(QMainWindow):
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
```

![image-20220302150203577](https://s2.loli.net/2022/03/02/ULl9jCwEmtb1OfM.png)

### 关闭窗口

```python
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QPushButton(string text, parent = None)
        # text参数是想要显示的按钮名称，parent参数是放在按钮上的组件，
        # 这个例子中，父级组件就是我们创建的继承自 Qwidget 的 Example 类。
        qbtn = QPushButton('Quit', self)
        # 事件传递系统在PyQt5内建的single和slot机制里面。点击按钮之后，信号会被捕捉并给出既定的反应。
        # QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例。
        # QCoreApplication是在QApplication里创建的。 点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        # 在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # qbtn.clicked.connect(self.close)    # 暂时认为是等价的

        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

![image-20220302150504521](https://s2.loli.net/2022/03/02/S2f6yk8Wm4tCjQH.png)

## QWidget

基础窗口控件QWidget类是所有用户界面对象的基类，所有的窗口和控件都直接或间接继承QWidget类。

窗口控件（Widget，简称“控件”）是在PyQt中建立界面的主要元素。

在PyQt中把没有嵌入到其他控件中的控件称为`窗口`，一般窗口都有边框、标题栏。

窗口是指程序的整体界面，可以包含标题栏、菜单栏、工具栏、关闭按钮、最小化按钮、最大化按钮等；

控件是指按钮、复选框、文本框、表格、进度条等这些组成程序的基本元素。

一个程序可以有多个窗口，一个窗口也可以有多个控件。

### 基本函数调用方法

```python
# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QSize

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
```

> 需要注意的是，窗口和控件都继承自`QWidget`类，如果不为控件指定一个父对象，那么该控件就会被当作窗口处理，这时`setWindowTitle()` 和 `setWindowIcon()` 函数就会生效。

### 高级函数用法

```python
# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QWidget_Func")
        # == 设置气泡提示
        # == 静态方法设置字体
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip("这是一个<b>气泡提示</b>")
        # =================


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WinForm()
    w.show()
    sys.exit(app.exec_())
```

## QLabel

QLabel对象作为一个占位符可以显示不可编辑的文本或图片，也可以放置一个GIF动画，还可以被用作提示标记为其他控件。

纯文本、链接或富文本可以显示在标签上。

```python
# 继承关系如下
QObject 
	|
    +--	QPaintDevice 
        	 |	   
             +-- QWidget
                	|		 
                    +--	QFrame
                          |			 
                          +-- QLabel
```

### 常用方法

```python
from PyQt5.QtCore import Qt
```

|          方法          |                             描述                             |
| :--------------------: | :----------------------------------------------------------: |
|     setAlignment()     |                    按固定值方式对齐文本：                    |
|                        | 水平方向：`Qt.AlignLeft`,`Qt.AliginRight`,`Qt.AliginCenter`,`Qt.AlignJustify(两端对齐)` |
|                        |  垂直方向：`Qt.AlignTop`,`Qt.AlignBottom`,`Qt.AlignVCenter`  |
|      setPixmap()       |                设置`QLabel`为一个`Pixmap`图片                |
| setOpenExternalLinks() |               打开允许访问超链接，默认是不允许               |
|       setBuddy()       | 设置`QLabel`的助记符及`buddy`（伙伴），即使用QLabel设置快捷键，会在快捷键后将焦点设置到其buddy上。此外，buddy可以是任何一个Widget控件，其QLabel必须是文本内容，并且使用“&”符号设置了助记符。 |
|        **信号**        |                           **描述**                           |
|    linkActivated()     | 单击`label`中嵌入的超链接时触发，`setOpenExternalLinks`必须设置为False |
|     linkHovered()      | 当鼠标指针滑过`label`的超链接时触发，`label`必须有超链接才可以 |

## QLineEdit

## QTextEdit

## QPushButton

QPushButton 类继承自 QAbstractButton 类，形状是长方形，文本标题或图标可以显示在长方形上。它也是一种命令按钮，可以单击该按钮执行一些命令，或者响应一些事情。常见的有“确认”，“申请“，”取消“，”关闭“，“是”，“否”等按钮。

### 设置快捷键

比如按钮名字为 `"&Download"` 的快捷键是 `Alt + D` 。其规则是：按钮中有这个字母，并且字母前面加上“&”，这个字母一般是首字母，而且“&”不会被显示出来，但字母会显示一条下划线。

## QRadioButton

QRadioButton类继承自QAbstractButton类，它提供了一组可供选择的按钮和文本标签，用户可以选择其中一个选项，标签用于显示对应的文本信息。

单选钮是一种开关按钮，可以切换为on或者off，即checked或者unchecked，主要是为用户提供“多选一”的选择。

QRadioButton 是单选钮控件默认是独占的（Exclusive）。对于继承自同一个父类 Widget 的多个单选钮，它们属于同一个按钮组合，在单选钮组里，一次只能选择一个单选钮。如果需要多个独占的按钮组合，则需要将它们放在 QGroupBox 或 QButtonGroup 中。

当将单选钮切换到 on 或者 off 时，就会发送 toggled 信号，绑定这个信号，在按钮状态发生变化时，触发相应的行为。

常用方法：

|    方法     |              描述               |
| :---------: | :-----------------------------: |
| isChecked() | 返回单选钮状态 ： True 或 False |
|             |                                 |
|             |                                 |

## QCheckBox

## QComboBox

## QSpinBox

## QSlider

## QDialog

## QMessageBox

## QInputDialog

## QFontDialog

## QFileDialog

QFileDialog 是用于打开和保存文件的标准对话框，继承自QDialog类。

QFileDialog 使用了文件过滤器，用于显示指定扩展名的文件。也可以设置使用QFileDialog打开文件时的起始目录和指定扩展名的文件。

|       方法        |                             描述                             |
| :---------------: | :----------------------------------------------------------: |
|   setFileMode()   | QFileDialog.AnyFile ： 任何文件 \|\| QFileDialog.ExistingFile ：已存在的文件 |
|                   | QFileDialog : Directory ：文件目录 \|\| QFileDialog.ExistingFiles ：已存在的多个文件 |
|  selectedFiles()  |                    返回一个选择的文件列表                    |
| getOpenFileName() | 打开文件，返回文件名和过滤词缀 `(self, 'Open file', ".", "(*.py *.ui)")` |

```python
# -*- coding: UTF-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QGridLayout


class Ui_Form(object):
    def setupUi(self, Form):
        self.layout = QGridLayout()
        self.PushButton_Directory = QPushButton(Form)
        self.PushButton_Directory.setText("&Directory")
        self.PushButton_File = QPushButton(Form)
        self.PushButton_File.setText("&File")
        Form.resize(300, 160)
        self.layout.addWidget(self.PushButton_Directory)
        self.layout.addWidget(self.PushButton_File)
        Form.setLayout(self.layout)


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 比较固定的初始化调用方式
        self.PushButton_Directory.clicked.connect(self.getDir)
        self.PushButton_File.clicked.connect(self.getFile)

    def getDir(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)
        if dlg.exec_():
            dir_name = dlg.selectedFiles()
            print(dir_name)

    def getFile(self):
        dir_name, _ = QFileDialog.getOpenFileName(self, 'Open file', ".", "(*.py *.ui)")
        print(dir_name)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
```

# PyQt5 高级界面控件

## QTableView

​	一个应用需要和一批数据（比如数组，列表）进行交互，然后以表格的形式输出这些信息，这时就要用到QTableView类了，在QTableView中可以使用自定义的数据模型在显示内容，通过setModel来绑定数据源。

​	QTableWidget 继承自 QTableView，主要区别是 QTableView 可以使用自定义的数据模型来显示内容，而QTableWidget只能使用标准的数据模型，并且其单元格数据是通过 QTableWidgetItem 对象来实现的。通常使用 QTableWidget 就能够满足我们的需求。

​	QTableView 控件可以绑定一个模型数据用来更新控件上的内容，可用的模式如下表所示：

| 名称 | 含义 |
| ---- | ---- |
|      |      |
|      |      |
|      |      |

```python
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# TODO: Page242
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(500, 300)
        # 创建一个标准数据model
        self.model = QStandardItemModel(4, 4)
        self.HeaderLabels = ["标题1", "标题2", "标题3", "标题4"]
        self.model.setHorizontalHeaderLabels(self.HeaderLabels)
        # 将model装填数据
        for row in range(4):
            for col in range(len(self.HeaderLabels)):
                item = QStandardItem("row %s, col %s" % (row, col))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)    # 可以设置居中之类的
                self.model.setItem(row, col, item)
        # 创建一个 QTableView 对象
        self.tableView = QTableView(Form)
        # 将数据模型装载进去
        self.tableView.setModel(self.model)

        # self.tableView.horizontalHeader().setStretchLastSection(True)   # 最后一节填充
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)     # 每列都平均填充

        # 添加数据
        # 添加数据 == 填充一行数据
        self.model.appendRow([
            QStandardItem("xxx"),
            QStandardItem("xxx"),
            QStandardItem("xxx"),
            QStandardItem("xxx")
        ])
        # 添加数据 == 只添加单个数据就只会填充一格, 两个数据就只会填充两格
        self.model.appendRow([QStandardItem("yyy"), QStandardItem("zzz")])


        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        Form.setLayout(dlgLayout)


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 比较固定的初始化调用方式
        print(self.HeaderLabels)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())

```

![image-20220427135140238](https://s2.loli.net/2022/04/27/kFDE3Q9TbWXPyuO.png)

1. 需要表格填满窗口

   ```python
   self.tableView.horizontalHeader().setStretchLastSection(True)   # 最后一节填充
   self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)     # 每列都平均填充
   ```

2. 删除数据

   ```python
   # 删除数据,需要选中
   # 删除数据 == 第一种
   indexs = self.tableView.selectionModel().selection().indexes()
   if len(indexs) > 0:
       index = indexs[0]
       self.model.removeRows(index.row(), 1)
   # 删除数据 == 第二种
   index = self.tableView.currentIndex()
   self.model.removeRows(index.row())
   ```

## QListView

## QListWidget

## QTableViewWidget

​	QTableWidget 是QT程序中常用的显示数据表格的空间，很类似于VC、C#中的DataGrid。说到QTableWidget，就必须讲一下它跟QTabelView的区别了。

​	QTableWidget 是 QTableView 的子类，主要的区别是 QTableView 可以使用自定义的数据模型来显示内容(也就是先要通过setModel来绑定数据源)，而 QTableWidget 则只能使用标准的数据模型，并且其单元格数据是QTableWidgetItem的对象来实现的(也就是不需要数据源，将逐个单元格内的信息填好即可)。这主要体现在QTableView类中有setModel成员函数，而到了QTableWidget类中，该成员函数变成了私有。使用QTableWidget就离不开QTableWidgetItem。QTableWidgetItem用来表示表格中的一个单元格，正个表格都需要用逐个单元格构建起来。

| 区别点                  | QTableView                       | QTableWidget                                                 |
| :---------------------- | :------------------------------- | :----------------------------------------------------------- |
| 继承关系                |                                  | QTableWidget继承自QTableView                                 |
| 使用数据模型setModel    | 可以使用setModel设置数据模型     | setModel是私有函数，不难使用该函数设置数据模型               |
| 显示复选框setCheckState | 没有函数实现复选框               | QTableWidgetItem类中的setCheckState(Qt::Checked);可以设置复选框 |
| 与QSqlTableModel绑定    | QTableView能与QSqlTableModel绑定 | QtableWidget不能与QSqlTableModel绑定                         |

- 两个遍历的区别

```python
# qtableView遍历
for i in range(self.model.rowCount()):
    for j in range(self.model.columnCount()):
        c = self.model.data(self.model.index(i,j))
        print(c)

# qtablewidget遍历
for i in range(self.tablewidget.rowCount()):
    for j in range(self.tablewidget.columnCount()):
        tb1.append(self.tablewidget.item(i,j).text())
```

### Base

```python
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# TODO: Page248
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(500, 300)
        self.HeaderLabels = ["标题1", "标题2", "标题3", "标题4"]
        # 创建一个 QTableWidget 对象
        self.tableWidget = QTableWidget(Form)
        # 创建一个 QTableWidget 对象 == 设置行列
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(4)
        # 创建一个 QTableWidget 对象 == 设置标签
        self.tableWidget.setHorizontalHeaderLabels(self.HeaderLabels)
        self.tableWidget.setVerticalHeaderLabels(['a', 'b', 'c', 'd'])
        # 用 QTableWidgetItem 装填数据
        for row in range(4):
            for col in range(len(self.HeaderLabels)):
                # QTableWidget 必须用自己的 Item 装填数据， setModel() 变为了私有方法
                item = QTableWidgetItem("row %s, col %s" % (row, col))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)    # 可以设置居中之类的
                self.tableWidget.setItem(row, col, item)
        # 格式设置
        # self.tableView.horizontalHeader().setStretchLastSection(True)   # 最后一节填充
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)     # 每列都平均填充
        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableWidget)
        Form.setLayout(dlgLayout)


class MyMainForm(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)  # 比较固定的初始化调用方式
        print(self.HeaderLabels)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
```

# PyQt5_Tutorial

## QObject

*The base class of all Qt objects*

QObject是Qt对象模型的核心。这个模型的中心特性是一个非常强大的无缝对象通信机制，称为信号和插槽。可以使用connect()将信号连接到槽位，也可以使用disconnect()销毁连接。

### 基础方法

```python
.setObjectName(str)	# 设置对象名
.objectName()		# 获取对象名，初始为空
```

### Property

```python
.setProperty(self, str, Any) -> bool	# 设置属性和值
.property(self, str) -> Any				# 获取属性的值
.dynamicPropertyNames(self) -> List[QByteArray]		# 获取所有的属性名称，返回的是Qt对象
```

**示例：**

```python
def func(self):
    self.object.setProperty('level1', '第一')     # 给对象添加一个属性和值
    tempList = [1, 2, 3, 4, 5]
    self.object.setProperty('level2', tempList)
    print(self.object.property('level1'))       # 获取属性对应的值，没有返回None，相当于字典
    print(self.object.property('level2'))
    print(self.object.dynamicPropertyNames())	# 获取所有的属性名称，返回的是Qt对象
    
# 第一
# [1, 2, 3, 4, 5]
# [PyQt5.QtCore.QByteArray(b'level1'), PyQt5.QtCore.QByteArray(b'level2')]
```

- 获取 **dynamicPropertyNames()** 所有 data

```python
l = self.object.dynamicPropertyNames()
# 获取byte
l[0].data()
# 获取str
l[0].data().decode()
```

### 对象间的父子关系

```python
.setParent(self, QObject)		# 设置爸爸
.parent(self) -> QObject		# 返回爸爸
# 此处没有 设置儿子 方法
.children(self) -> List[QObject]	# 返回儿子列表

# findChild()
# 找寻直接子类, type 是指 QObject, QWidget.. 等等，但是不用用 type=QObject, 会报错
.findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject
.findChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject

# findChildren()
# 找寻所有符号条件的子类，返回子类列表
.findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
.findChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
.findChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
.findChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
.findChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
.findChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]
```

**示例：**

```python
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
```

## PyQt5.QtWidgets

`PyQt5.QtWidgets` 模块包含了基本的组件。

### QApplication

每个PyQt5应用都必须创建一个应用对象

```python
import sys
from PyQt5.QtWidgets import QApplication
# sys.argv是一组命令行参数的列表。Python可以在shell里运行，这个参数提供对脚本控制的功能
app = QApplication(sys.argv)
# 当调用exit()方法或直接销毁主控件时，主循环就会结束。sys.exit()方法能确保主循环安全退出。外部环境能通知主控件怎么结束。
sys.exit(app.exec_())
```

### QWidget

- 创建对象

  ```python
  from PyQt5.QtWidgets import QWidget
  
  class QWidget(__PyQt5_QtCore.QObject, __PyQt5_QtGui.QPaintDevice):
      """ QWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) """
      
  # 直接创建
  w = QWidget()
  
  # 用对象继承
  class Example(QWidget):
      def __init__(self):
          super().__init__()
          self.initUI()
  
      def initUI(self):
          # 使用继承自QWidget类的方法
          self.setGeometry(300, 300, 300, 220)
          self.setWindowTitle('Icon')
          self.setWindowIcon(QIcon('..\\..\\image\\Globe.ico'))
          self.show()
  ```

#### .centralWidget()

```python
# 返回窗口中心的一个控件，未设置时返回NULL
centralWidget(self) -> QWidget
```

#### .close()

```python
close(self) -> bool		# 退出组件
```

#### .closeEvent()

```python
# 控件关闭时触发结束事件
closeEvent(self, QCloseEvent)

# 示例：
def closeEvent(self, event):
    # 第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，
    # 最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量reply里。
    reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.No)
    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
```

#### .mouseMoveEvent()

```python
mouseMoveEvent(self, QMouseEvent)
```

#### .frameGeometry()

```python
# 得到了窗口的大小
frameGeometry(self) -> QRect
```

#### .resize()

```python
# 改变控件的大小
resize(self, QSize)
resize(self, int, int)		# 宽 和 高
```

#### .move()

```python
# 修改控件位置，注意屏幕的原点在左上角
move(self, QPoint)
move(self, int, int)
```

#### .setCentralWidget()

```python
# 设置窗口中心的控件
setCentralWidget(self, QWidget)

# 示例：
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
		self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
```

#### .setWindowTitle()

```python
# 窗口添加标题
setWindowTitle(self, str)
```

#### .show()

```python
# 让控件在桌面上显示出来,一般在类设置好后，最后调用显示
show(self)
```

#### .setGeometry()

```python
# setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。
# int x, int y, int w, int h	
setGeometry(self, QRect)
setGeometry(self, int, int, int, int)
```

#### .setWindowIcon()

```python
# 窗口左上角设置图标，参数为 QIcon 对象
setWindowIcon(self, QIcon)
```

#### .setToolTip()

```python
# 创建提示框可以使用富文本格式的内容。
setToolTip(self, str)

# 示例：
self.setToolTip('This is a <b>QWidget</b> widget')
```

#### .setLayout()

```python
setLayout(self, QLayout)
```

#### .setMouseTracking()	

```python
setMouseTracking(self, bool)
```

#### .sizeHint()

```python
# 提供一个默认的按钮大小
sizeHint(self) -> QSize
```

#### .QKeyEvent()

```python
keyPressEvent(self, QKeyEvent)

# 示例：
def keyPressEvent(self, e):
    if e.key() == Qt.Key_Escape:
        self.close()
```

### QAbstractButton

```python
class QAbstractButton(QWidget):
```

### QPushButton

```python
# text参数是想要显示的按钮名称，parent参数是放在按钮上的组件
class QPushButton(QAbstractButton):
# 示例：
QPushButton(parent: QWidget = None)
QPushButton(str, parent: QWidget = None)
QPushButton(QIcon, str, parent: QWidget = None)
```

#### .resize()

```python
# 改变控件的大小
resize(self, QSize)
resize(self, int, int)		# 宽 和 高
```

#### .move()

```python
# 修改控件位置，注意屏幕的原点在左上角
move(self, QPoint)
move(self, int, int)
```

#### .setToolTip()

```python
# 创建提示框可以使用富文本格式的内容。
setToolTip(self, str)

# 示例:
btn.setToolTip('This is a <b>QPushButton</b> widget')
```

#### .sizeHint()

```python
# 提供一个默认的按钮大小
sizeHint(self) -> QSize
```

### QDesktopWidget

```python
class QDesktopWidget(QWidget):
```

#### .availableGeometry()

```python
availableGeometry(self, screen: int = -1) -> QRect		# 获取显示器的分辨率
availableGeometry(self, QWidget) -> QRect
availableGeometry(self, QPoint) -> QRect
```

### QTableWidget

```python
class QTableWidget(QTableView):
    """
    QTableWidget(parent: QWidget = None)
    QTableWidget(int, int, parent: QWidget = None)
    """
```

#### BaseFunction

```python
#  QTableWidget
clear(self)					# 清除所有数据包括行列
clearContents(self)      	# 清除所有数据不包括行列
columnCount(self) -> int	# 返回行数
rowCount(self) -> int		# 返回行数
setShowGrid(self, bool)		# 显示网格线,默认True
setColumnWidth(self, int, int)		# 设置单元格列的宽度
setRowHeight(self, int, int)		# 设置单元格行的高度
setHorizontalHeaderLabels(self, Iterable[str])		# 设置水平标签
setVerticalHeaderLabels(self, Iterable[str])		# 设置垂直标签
setItem(self, int, int, QTableWidgetItem)			# 在单元空间内添加控件
horizontalHeader(self) -> QHeaderView		# 获得表格头，以便执行隐藏


# TODO
setSelectionBehavior(self, QAbstractItemView.SelectionBehavior)		# 设置表格的选择行为
```

#### .setRowCount() & .setColumnCount()

```python
setRowCount(self, int)			# 设置行数
setColumnCount(self, int)		# 设置列数
```

以行为例：

假设现在有 4 行数据，setRowCount(6) 后， 4 行数据会被保留，新增 2 行空行；

假设现在有 4 行数据，setRowCount(2) 后， 4 行数据 中的前 2 行会被保留；

假设现在有 4 行数据，setRowCount(2)  +  setRowCount(6) 后， 4 行数据 中的前 2 行会被保留，后面追加 4 行空行数据；

#### .setSpan()

```python
setSpan(self, int, int, int, int)		# 合并单元格
```

`setSpan(int row, int column, int rowSpanCount, int columnSpanCount)`

要改变单元格的第 **row** 行第 **column** 列，要合并 **rowSpanCount** 行数和 **columnSpanCount** 列数

#### .setEditTriggers()

```python
setEditTriggers(self, Union[QAbstractItemView.EditTriggers, QAbstractItemView.EditTrigger])		# 设置表格是否可编辑
```

- 设置编辑规则的枚举

```python
QAbstractItemView.NoEditTriggers	# 0		# 不能对表格内容进行修改
QAbstractItemView.CurrentChanged	# 1		# 任何时候都能修改
QAbstractItemView.DoubleClicked		# 2		# 双击修改
QAbstractItemView.SelectedClicked	# 4		# 单击已选中的内容
QAbstractItemView.EditKeyPressed	# 8		# 当修改键被按下时修改单元格
QAbstractItemView.AnyKeyPressed		# 16	# 按任意键修改单元格
QAbstractItemView.AllEditTriggers	# 31	# 包括以上所有条件
```

### QToolTip

#### .setFont

```python
# 静态方法;设置提示框的字体
setFont(QFont)

# 示例：
# 设置为10px的SansSerif字体
QToolTip.setFont(QFont('SansSerif', 10))
```

### QMessageBox

#### .question()

```python
# 第一个字符串显示在消息框的标题栏，第二个字符串显示在对话框，第三个参数是消息框的俩按钮，
# 最后一个参数是默认按钮，这个按钮是默认选中的。返回值在变量reply里。
question(QWidget, str, str, 
         buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No), 
         defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) 
		-> QMessageBox.StandardButton
    
# 示例：
reply = QMessageBox.question(self, 'Message', "Are you sure to quit?",
                             QMessageBox.Yes | QMessageBox.No,
                             QMessageBox.No)
```

### QMainWindow

`QMainWindow`提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏。

```python
class QMainWindow(QWidget):
```

#### .addToolBar()

```python
# 一般用于QMainWindow，添加工具栏
addToolBar(self, Qt.ToolBarArea, QToolBar)
addToolBar(self, QToolBar)
addToolBar(self, str) -> QToolBar

# 示例
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
```

#### .setCentralWidget()

```python
# 设置窗口中心的控件，这个组件或占满所有剩余的区域。
setCentralWidget(self, QWidget)

# 示例：
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
		self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
```
#### .setMenuBar()

```python
# 设置一个菜单栏
setMenuBar(self, QWidget)

# 示例：
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
		self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
```

#### .setStatusBar()

```python
# 设置一个状态栏
setStatusBar(self, QStatusBar)
# 示例：
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
```

#### .centralWidget()

```python
# 返回窗口中心的一个控件，未设置时返回NULL
centralWidget(self) -> QWidget
```

#### .menuBar()

```python
menuBar(self) -> QMenuBar		# 返回一个菜单栏对象
```

#### .statusBar()

```python
statusBar(self) -> QStatusBar		# 返回一个状态栏对象,同时开启状态栏显示

# 示例：
self.status = self.statusBar()
self.status.showMessage("这是状态栏显示", 5000)
```
#### .contextMenuEvent()

```python
contextMenuEvent(self, QContextMenuEvent)		# 右键菜单的函数重载
```

### QStatusBar

```python
# 状态栏对象
class QStatusBar(QWidget):
```

#### .showMessage()

```python
showMessage(self, str, msecs: int = 0)		# 状态栏显示信息
# str: 要显示的状态栏信息
# msecs：停留的时间（ms)，0代表一直显示
```

### QMenuBar

```python
# 菜单栏对象
class QMenuBar(QWidget):
```

#### .addAction()

```python
addAction(self, QAction)
addAction(self, str) -> QAction
addAction(self, QIcon, str) -> QAction
addAction(self, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
addAction(self, QIcon, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
```

### QMenu

```python
# 菜单对象
class QMenu(QWidget):

QMenu(parent: QWidget = None)
QMenu(str, parent: QWidget = None)
```

#### .addAction()

```python
addAction(self, QAction)
addAction(self, str) -> QAction
addAction(self, QIcon, str) -> QAction
addAction(self, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
addAction(self, QIcon, str, PYQT_SLOT, shortcut: Union[QKeySequence, QKeySequence.StandardKey, str, int] = 0) -> QAction
```

#### .addMenu()

```python
addMenu(self, QMenu) -> QAction
addMenu(self, str) -> QMenu
addMenu(self, QIcon, str) -> QMenu
```

### QToolBar

```python
class QToolBar(QWidget):

QToolBar(str, parent: QWidget = None)
QToolBar(parent: QWidget = None)
```

#### .addAction()

```python
addAction(self, QAction)
addAction(self, str) -> QAction
addAction(self, QIcon, str) -> QAction
addAction(self, str, PYQT_SLOT) -> QAction
addAction(self, QIcon, str, PYQT_SLOT) -> QAction
```

### QTextEdit

```python
class QTextEdit(QAbstractScrollArea):

QTextEdit(parent: QWidget = None)
QTextEdit(str, parent: QWidget = None)
```

### QLabel

```python
class QLabel(QFrame):

QLabel(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
```

#### .move()

```python
# 修改控件位置，位置相对于父类而不是屏幕
move(self, QPoint)
move(self, int, int)
```

#### .setOpenExternalLinks()

```python
# 打开允许访问超链接，默认是不允许
setOpenExternalLinks(self, bool)
```

#### .setAlignment()

```python
# 设置文本排版
setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag])

# 示例：
from PyQt5.QtCore import Qt
label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
label.setAlignment(Qt.AlignCenter)
```

#### .setBuddy()

```python
# 设置`QLabel`的助记符及`buddy`（伙伴），即使用QLabel设置快捷键，会在快捷键后将焦点设置到其buddy上。此外，buddy可以是任何一个Widget控件，其QLabel必须是文本内容，并且使用“&”符号设置了助记符。
setBuddy(self, QWidget)
```

#### .setPixmap()

```python
# 设置`QLabel`为一个`Pixmap`图片
setPixmap(self, QPixmap)

# 示例：
label.setPixmap(QPixmap("../../image/Globe.png"))
```

#### .setText()

```python
setText(self, str) 
```

#### .linkActivated()

```python
# 单击`label`中嵌入的超链接时触发，`setOpenExternalLinks`必须设置为False
linkActivated(self, str) [signal]
```

#### .linkHovered()

```python
# 当鼠标指针滑过`label`的超链接时触发，`label`必须有超链接才可以
linkHovered(self, str) [signal]
```

### QLineEdit

```python
class QLineEdit(QWidget):
    """
    QLineEdit(parent: QWidget = None)
    QLineEdit(str, parent: QWidget = None)
    """
```

### QLCDNumber

```python
class QLCDNumber(QFrame):
    """
    QLCDNumber(parent: QWidget = None)
    QLCDNumber(int, parent: QWidget = None)
    """
```

#### .display()

```python
display(self, str)
display(self, float)
display(self, in	t)
```

### QAbstractSlider

```python
class QAbstractSlider(QWidget):
    """ QAbstractSlider(parent: QWidget = None) """
```

#### .valueChanged()

```python
valueChanged(self, int) [signal]
```

### QSlider

```python
class QSlider(QAbstractSlider):
    """
    QSlider(parent: QWidget = None)
    QSlider(Qt.Orientation, parent: QWidget = None)
    """
```

#### .valueChanged()

```python
valueChanged(self, int) [signal]
```

## QtCore

`from PyQt5.QtWidgets import QName`

### QAction

`from PyQt5.QtWidgets import QAction`

`QAction`是菜单栏、工具栏或者快捷键的动作的组合

```python
class QAction(__PyQt5_QtCore.QObject):
    
QAction(parent: QObject = None)
QAction(str, parent: QObject = None)
QAction(QIcon, str, parent: QObject = None)

# 示例：
viewStatAct = QAction('View statusbar', self, checkable=True)  # checkable 可选中的对象
```

#### .setShortcut()

```python
# 设置快捷键
setShortcut(self, Union[QKeySequence, QKeySequence.StandardKey, str, int])

# 示例：
setShortcut('Ctrl+Q')
```

#### .setStatusTip()

```python
setStatusTip(self, str)		# 设置状态栏显示
```

#### .setCheckable()

```python
setCheckable(self, bool)		# 设置是否为可选中的对象
```

#### .setChecked()

```python
setChecked(self, bool)		# 设置默认选中状态
```

#### .triggered()

```python
triggered(self, checked: bool = False) [signal]		# 触发一个信号

# 示例：
exitAct.triggered.connect(qApp.quit)
```

### Qt

#### 文本对齐方式

```python
# 水平对齐
Qt.AlignLeft		# 1		# 左对齐
Qt.AlignRight		# 2		# 右对齐
Qt.AlignHCenter		# 4		# 水平居中
Qt.AlignJustify		# 8		# 可用空间中对齐

# 垂直对齐
Qt.AlignTop			# 32	# 顶部对齐
Qt.AlignBottom		# 64	# 底部对齐
Qt.AlignVCenter		# 128	# 垂直居中
Qt.AlignBaseline	# 256	# 基线对齐
```

## QLayout

`from PyQt5.QtWidgets import QName`

```python
class QLayout(__PyQt5_QtCore.QObject, QLayoutItem):
    """
    QLayout(QWidget)
    QLayout()
    """
    
class QBoxLayout(QLayout):
    """ QBoxLayout(QBoxLayout.Direction, parent: QWidget = None) """
```

### QBoxLayout

```python
class QBoxLayout(QLayout):
    """ QBoxLayout(QBoxLayout.Direction, parent: QWidget = None) """
```

#### .addLayout()

```python
addLayout(self, QLayout, stretch: int = 0)
```

### QHBoxLayout

```python
class QHBoxLayout(QBoxLayout):
    
QHBoxLayout()
QHBoxLayout(QWidget)
```

### QGridLayout

```python
class QGridLayout(QLayout):
    @typing.overload
    def __init__(self, parent: QWidget) -> None: ...
    @typing.overload
    def __init__(self) -> None: ...
```

#### .addWidget()

```python
def addWidget(self, w: QWidget) -> None: ...
def addWidget(self, a0: QWidget, row: int, column: int, alignment: typing.Union[QtCore.Qt.Alignment, QtCore.Qt.AlignmentFlag] = ...) -> None: ...
# （窗口控件，行位置，列位置，要合并的行数，要合并的列数） 后两个是可选参数
def addWidget(self, a0: QWidget, row: int, column: int, rowSpan: int, columnSpan: int, alignment: typing.Union[QtCore.Qt.Alignment, QtCore.Qt.AlignmentFlag] = ...) -> None: ...
```

#### .addStretch()

```python
addStretch(self, stretch: int = 0)	# 在布局器中增加一个伸缩量，将nLayout的布局器的空白空间平均分配
```

#### .setSpacing()

```python
# 各个控件之间的上下间距
def setSpacing(self, spacing: int) -> None: ...
```

## __sip.simplewrapper

### QRect

```python
class QRect(__sip.simplewrapper):

QRect()
QRect(int, int, int, int)	# topLeft.x, topLeft.y, bottomRight.x, bottomRight.y 
QRect(QPoint, QPoint)		# 左上, 右下
QRect(QPoint, QSize)
QRect(QRect)
```

#### 基础调用

```python
adjust(self, int, int, int, int)		# ？
adjusted(self, int, int, int, int) -> QRect		# ？
bottom(self) -> int				# 返回控件的长
height(self) -> int				# 返回控件的高
bottomLeft(self) -> QPoint		# 返回左下点
bottomRight(self) -> QPoint		# 返回右下点
topLeft(self) -> QPoint			# 返回左上点
topRight(self) -> QPoint		# 返回右上点
center(self) -> QPoint			# 返回中心点
moveCenter(self, QPoint)		# 将中心点移动到QPoint
```

### QPoint

```python
class QPoint(__sip.simplewrapper):

QPoint()
QPoint(int, int)
QPoint(QPoint)
```

#### 基础调用

```python
x(self)
y(self)
setX(self, int)
setY(self, int)
dotProduct(QPoint, QPoint) -> int		# ?
manhattanLength(self) -> int			# 曼哈顿长度？
transposed(self) -> QPoint				# x,y 互换
```

## PyQt5.QtCore

### QCoreApplication

