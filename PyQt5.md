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

  如果搜索不到，就在 `...\miniconda3\Lib\site-packages\qt5_applications\Qt\bin\designer.exe` 路径下

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

基础窗口控件QWidget类是 **所有可视控件对象的基类**，所有的窗口和控件都直接或间接继承QWidget类。

窗口控件（Widget，简称“控件”）是在PyQt中建立界面的主要元素。

在PyQt中把没有嵌入到其他控件中的控件称为`窗口`，一般窗口都有边框、标题栏。

窗口是指程序的整体界面，可以包含标题栏、菜单栏、工具栏、关闭按钮、最小化按钮、最大化按钮等；

控件是指按钮、复选框、文本框、表格、进度条等这些组成程序的基本元素。

一个程序可以有多个窗口，一个窗口也可以有多个控件。

### Tips

1. **继承** 会有点问题，比如格式无法生效，需要手动设置 `self.setAttribute(Qt.WA_StyledBackground, True)`

或者一劳永逸，重写 `paintEvent()` 函数， C++ 也需要重构函数。

```python
def paintEvent(self, event):
    # 以下几行代码的功能是避免在多重传值后的功能失效
    opt = QStyleOption()
    opt.initFrom(self)
    p = QPainter(self)
    self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
```

### 控件的创建

```python
QWidget(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
.__init__(self, parent=None, flags, Qt_WindowFlags=None, Qt_WindowType=None, *args, **kwargs):
# parent: 父控件
# flags: 标志位	# 后面再讲
```

```python
# 如果没有父控件，就会被默认为顶层窗口，需要调用 show() 才能显示在桌面
window = QWidget()
window.show()
```

### 大小位置

#### 控件的坐标系统

![image-20220509105129872](https://s2.loli.net/2022/05/09/nvKwY5rLFsOxz7j.png)

以左上角为坐标原点，如果为顶层窗口，就以桌面为坐标系，否则就以父控件为坐标系。

#### 获取

![image-20220509105546923](https://s2.loli.net/2022/05/09/6UrEeLWkIt3xb7X.png)

如果为顶层窗口，不仅包括了用户区域（图中红线），还包括了外部框架的区域（图中绿线），使用API时注意区分。

`move()` 移动的坐标是包含 **窗口框架** 的。

```python
def testFunc1(q: QWidget):
    print(f"包含框架的坐标：{q.x(), q.y(), q.pos()}")
    print(f"包含框架的宽和高：{q.frameGeometry().width(), q.frameGeometry().height(), q.frameSize()}")
    print(f"用户区域的坐标：{q.geometry().x(), q.geometry().y(), q.geometry(), q.size(), q.rect()}")
    print(f"用户区域的宽和高：{q.width(), q.height()}")
```

- **.x() & .y() & .pos()**

包含窗口框架，注意获取坐标时，需要待窗口绘制完成后再获取，不然就会获取初始值。

```python
.x(self) -> int
.y(self) -> int
.pos(self) -> QPoint

# .pos().x() == .x() && .pos().y() == .y()
```

- **.frameGeometry()**

包含框架的宽和高

```python
.frameGeometry(self) -> QRect
.frameSize(self) -> QSize
```

- **.geometry()**

用户区域相当于父控件的位置和尺寸的组合

```python
.geometry(self) -> QRect

# QRect(x, y, width, height)
```

- **.width() & .height()**

用户区域的宽和高

```python
.width(self) -> int
.height(self) -> int
.size(self) -> QSize
.rect(self) -> QRect	# 单纯的只包含宽和高 QRect(0, 0, width, height)

# .width() == .geometry().width() && .height() == .geometry().height()
```

#### 设置

**注意：** 但凡涉及 `.move()` 的， `.show()` 以后  `.move()` 就失效了。

- **.move()**

操控的是 `x`, `y`；也就是 `pos`，包括窗口框架

```python
.move(self, QPoint)
.move(self, int, int)
```

- **.resize()**

操控的是宽，高，不包括窗口框架。

**注意：** `.resize()` 不能小于控件的 最小尺寸

```python
.resize(self, QSize)
.resize(self, int, int)
```

- **.setGeometry()**

`.setGeometry(x_noFrame, y_noFrame, width, height)`

用户区域

```python
.setGeometry(self, QRect)
.setGeometry(self, int, int, int, int)
```

- **.adjustSize()**

```python
.adjustSize(self)	# 根据内容自适应大小,优先级很低
```

- **.setFixedSize()**

固定尺寸，优先级很高

```python
.setFixedSize(self, QSize)
.setFixedSize(self, int, int)
```

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/9 15:54"
"""

"""
Example：
通过给定的个数，负责在一个窗口内创建相应个数的子控件。
要求：控件按照九宫格的布局进行摆放。
"""

from PyQt5.Qt import *
import sys

__author__ = "Jacob-xyb"

import sys
from PyQt5.Qt import *


class BaseWidget(QWidget):
    def __init__(self, parent=None, x=10, y=10):
        super().__init__(parent)
        self.resize(x, y)

    def paintEvent(self, event):
        # 以下几行代码的功能是避免在多重传值后的功能失效
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)


class Btn(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example1")
        self.totalCol = 3
        self.setup_ui()

    def setup_ui(self):
        inputNums = 66
        if inputNums % self.totalCol:
            self.totalRow = inputNums // self.totalCol + 1
        else:
            self.totalRow = inputNums // self.totalCol
        # 先设置顶层控件的尺寸
        temp_x, temp_y = 100, 20
        self.resize(self.totalCol * temp_x, self.totalRow * temp_y)
        # 开始添加控件
        for i in range(inputNums):
            temp_qwidget = BaseWidget(self, temp_x, temp_y)
            temp_qwidget.setStyleSheet("background-color: red;border: 1px solid yellow")
            pos_x = (i % self.totalCol) * temp_x
            pos_y = (i // self.totalCol) * temp_y
            temp_qwidget.move(pos_x, pos_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

![image-20220509155425546](https://s2.loli.net/2022/05/09/FOlnwmHpau9cs7y.png)

### 最大最小尺寸

#### 获取

```python
.minimumWidth(self) -> int
.minimumHeight(self) -> int
.minimumSize(self) -> QSize
.maximumWidth(self) -> int
.maximumHeight(self) -> int
.maximumSize(self) -> QSize
```

#### 设置

```python
.setMinimumSize(self, int, int)
.setMinimumSize(self, QSize)
.setMinimumWidth(self, int)
.setMinimumHeight(self, int)
.setMaximumSize(self, int, int)
.setMaximumSize(self, QSize)
.setMaximumWidth(self, int)
.setMaximumHeight(self, int)
```

### 内容边距

调整内容边距后，只在内容范围内显示内容。

#### 获取

```python
.contentsRect(self) -> QRect
```

#### 设置

```python
.setContentsMargins(self, int, int, int, int)	# 0代表默认值
.setContentsMargins(self, QMargins)
```

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/9 21:07"
"""

"""
Example：
创建一个窗口，包含一个标签，标签内容为：Hello Jx
标签大小为100,60; 将标签文字放置在标签右下角
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example2")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.resize(100, 60)
        self.label.setText("Hello Jx")
        self.label.setStyleSheet("background-color: cyan")
        self.label.setContentsMargins(50, 30, 0, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

### 鼠标相关

#### 设置鼠标形状

```python
.setCursor(self, Union, QCursor=None, Qt_CursorShape=None)
.setCursor(self, Union[QCursor, Qt.CursorShape])
.unsetCursor(self)

# example:
.setCursor(Qt.BusyCursor)
```

- **自定义鼠标**

```python
QCursor()
QCursor(QBitmap, QBitmap, hotX: int = -1, hotY: int = -1)
QCursor(QPixmap, hotX: int = -1, hotY: int = -1)	# 最常用,hotX 代表热点在图片中心
QCursor(Union[QCursor, Qt.CursorShape])
QCursor(Any)
```

#### 鼠标位置

```python
cursor(self) -> QCursor		# 获取鼠标对象
.pos() -> QPoint		# 默认相对于桌面的坐标位置	
.pos(QScreen) -> QPoint

# 设置鼠标位置
.setPos(int, int)
.setPos(QPoint)
.setPos(QScreen, int, int)
.setPos(QScreen, QPoint)

.pixmap(self) -> QPixmap	# 获取鼠标图片
```

#### 鼠标跟踪

如果没有开启鼠标跟踪，则只有当鼠标处于激活状态（按住左键、右键、中键等）才会触发 move 事件。

```python
def mouseMoveEvent(self, a0: QMouseEvent) -> None:
    print("鼠标移动了")
    return super().mouseMoveEvent(a0)
```

开启后就可以实时触发事件

```python
print(q.hasMouseTracking())     # 默认是 False
q.setMouseTracking(True)            # 设置为跟踪状态
```

`QMouseEvent` 里面可以获取 全局 和 局部 的坐标。

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 10:53"
"""

"""
Example：
创建一个窗口，包含一个标签，标签随鼠标位置移动，鼠标设置为指定图标
"""

import sys
from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example3")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # 先创建好一个标签对象
        self.label = QLabel(self)
        self.label.resize(60, 20)
        self.label.setText("Hello Jx")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: red")
        # 再把鼠标设置一下
        cursor = QCursor(QPixmap("Globe.ico").scaled(20, 20), 0, 0)
        self.setCursor(cursor)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        self.label.move(e.x(), e.y())
        return super().mouseMoveEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

### 事件

#### 基础事件

```python
def showEvent(self, e: QShowEvent) -> None:
    print("窗口开始展示，触发showEvent事件")
    return super(Window, self).showEvent(e)

def closeEvent(self, e: QCloseEvent) -> None:
    print("触发closeEvent事件")
    return super(Window, self).closeEvent(e)

# 窗口移动判定的是窗口的左上角坐标
def moveEvent(self, e: QMoveEvent) -> None:
    print("窗口被移动")  # show() 时就会打印一次
    return super(Window, self).moveEvent(e)

def resizeEvent(self, e: QResizeEvent) -> None:
    print("窗口改变了尺寸大小")  # show() 时也会触发一次
    return super(Window, self).resizeEvent(e)

# 鼠标进来和离开事件 判定范围 不包括标题区域
def enterEvent(self, e: QEvent) -> None:
    print("鼠标进来了")
    return super(Window, self).enterEvent(e)

def leaveEvent(self, e: QEvent) -> None:
    print("鼠标离开了")
    return super(Window, self).leaveEvent(e)

def mousePressEvent(self, e: QMouseEvent) -> None:
    print("鼠标被按下")
    return super(Window, self).mousePressEvent(e)

def mouseReleaseEvent(self, e: QMouseEvent) -> None:
    print("鼠标被释放了")
    return super(Window, self).mouseReleaseEvent(e)

def mouseDoubleClickEvent(self, e: QMouseEvent) -> None:
    print("鼠标双击")
    return super(Window, self).mouseDoubleClickEvent(e)

def keyPressEvent(self, e: QKeyEvent) -> None:
    print("键盘上某一个按键被按下")
    return super(Window, self).keyPressEvent(e)

def keyReleaseEvent(self, e: QKeyEvent) -> None:
    print("键盘上某一个按键被释放")
    return super(Window, self).keyReleaseEvent(e)

# 获取焦点时调用
def focusInEvent(self, e: QFocusEvent) -> None:
    return super(Window, self).focusInEvent(e)

# 失去焦点时调用
def focusOutEvent(self, e: QFocusEvent) -> None:
    return super(Window, self).focusOutEvent(e)

...

dragEnterEvent()	# 拖拽进入控件时调用
dragLeaveEvent()	# 拖拽离开控件时调用
dragMoveEvent()		# 拖拽在控件内移动时调用
drogEvent()			# 拖拽放下时调用

paintEvent()		# 显示或者更新控件时调用
changeEvent()		# 窗体改变，字体改变时调用
contextMenuEvent()	# 访问右键菜单时调用

inputMethodEvent()	# 输入法调用
```

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 13:49"
"""

"""
Example：
创建一个窗口，包含一个标签。
鼠标移动进来时和出去时的文字不一样；
然后能捕捉快捷键：tab, ctrl+s, ctrl+shift+a
"""

import sys
from PyQt5.Qt import *

class Label(QLabel):
    def enterEvent(self, e: QEvent) -> None:
        self.setText("欢迎光临！")
        return super(Label, self).enterEvent(e)

    def leaveEvent(self, e: QEvent) -> None:
        self.setText("谢谢惠顾！")
        return super(Label, self).leaveEvent(e)

    def keyPressEvent(self, ev: QKeyEvent) -> None:
        # 按下单个键
        if ev.key() == Qt.Key_Tab:
            self.setText("按下了 Tab 键")
        # 按下组合键，就要分修饰符和普通键位
        elif ev.modifiers() == Qt.ControlModifier and ev.key() == Qt.Key_S:
            self.setText("按下了 Ctrl+S 键")
        # 如果是多个组合键，用 或| 运算符运算
        elif ev.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and ev.key() == Qt.Key_A:
            self.setText("按下了 Ctrl+Shift+A 键")
        return super(Label, self).keyPressEvent(ev)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example3")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # 先创建好一个标签对象
        self.label = Label(self)
        self.label.resize(100, 80)
        self.label.move(200, 100)
        self.label.setText("Hello Jx")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: red")
        self.label.grabKeyboard()       # 捕获全局键盘


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

### 父子控件

```python
.childAt(x, y)
.parentWidget()
.childrenRect()		# 所有子控件组成的边界矩形
```

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/10 14:16"
"""

"""
Example：
创建一个窗口，包含十个标签。
利用父类实现：点击哪个标签就改变哪个标签的背景颜色。
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example5")
        self.resize(600, 400)
        self.setup_ui()

    def setup_ui(self):
        # 先创建好一个标签对象
        for i in range(1, 11):
            label = QLabel(self)
            label.resize(100, 20)
            label.setAlignment(Qt.AlignCenter)
            label.move(40 * i, 20 * i)
            label.setText(f"标签 {i}")

    def mousePressEvent(self, e: QMouseEvent) -> None:
        tempWidget = self.childAt(e.localPos().toPoint())
        if tempWidget:
            tempWidget.setStyleSheet("background-color: red;")
        return super(Window, self).mousePressEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

### 层级控制

调整控件z轴顺序

```python
.lower()		# 将控件降低到最底层
.raise_()		# 将控件提升到最上层
a.stackUnder(b)	# 让a放到b下面（a，b同级）
```

### 顶层窗口相关

#### 图标设置

```python
.setWindowIcon(QIcon(str))		# 设置窗口图标
.setWindowTitle(str)			# 设置标题
.windowTitle()		# 获取标题
```

#### 不透明度

```python
.setWindowOpacity(float)		# 不透明度： 0.0 ~ 1.0
.windowOpacity()		# 获取不透明度
```

#### 窗口状态

```python
.windowState()		# 获取窗口状态
.setWindowState(state)		# 设置窗口状态
"""
state:
	Qt.WindowNoState		无状态
	Qt.WindowMinimized		最小化
	Qt.WindowMaximized		最大化
	Qt.WindowFullScreen		全屏
	Qt.WindowActive			活动窗口
"""
```

#### 最大化最小化

```python
.showFullScreen()
.showMaximized()
.showMinimized()
.showNormal()
.isMinimized()
.isMaximized()
.isFullScreen()
```

#### 窗口标志

```python
window.setWindowFlags(Qt.WindowStaysOnTopHint)
"""
Flag:
	Qt.FramelessWindowHint		窗口无边框
	Qt.MSWindowsFixedSizeDialogHint		窗口无法调整大小
	Qt.CustomizeWindowHint		有边框但无标题栏和按钮，不能移动和拖动
	Qt.WindowTitleHint			添加标题栏和一个关闭按钮
	Qt.WindowSystemMenuHint		添加系统目录和一个关闭按钮
	Qt.WindowMaximizeButtonHint	激活最大化和关闭按钮，禁止最小化按钮
"""
```

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/11 9:52"
"""

"""
Example：
创建一个窗口，无边框无标题栏，窗口半透明，自定义最小化，最大化，关闭按钮，支持拖拽用户区移动
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example5")
        self.dragFlag = False
        self.current_pos = None
        self.current_widget_pos = None
        self.setup_ui()
        self.resize(600, 400)

    def setup_ui(self):
        self.setWindowOpacity(0.5)      # 设置窗口半透明
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 创建三个子控件按钮
        self.btn_minimum = QPushButton(self)
        self.btn_minimum.setText("最小化")
        self.btn_maximum = QPushButton(self)
        self.btn_maximum.setText("最大化")
        self.btn_close = QPushButton(self)
        self.btn_close.setText("关闭")
        # 如果不手动 resize，就会有问题：第一次调用的 width 与实际的 width 不一致
        self.btn_minimum.resize(75, 25)
        self.btn_maximum.resize(75, 25)
        self.btn_close.resize(75, 25)
        # 设置功能
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_minimum.clicked.connect(lambda: self.showMinimized())
        self.btn_maximum.clicked.connect(lambda: self.btnMaxClickEvent())

    def btnMaxClickEvent(self):
        if self.windowState() == Qt.WindowNoState:
            self.btn_maximum.setText("缩放窗口")
            self.showMaximized()
        else:
            self.btn_maximum.setText("最大化")
            self.showNormal()

    def resizeEvent(self, e: QResizeEvent) -> None:
        # 摆放这些按钮
        width = self.width()
        btn_close_x = width - self.btn_close.width()
        btn_close_y = 10
        self.btn_close.move(btn_close_x, btn_close_y)
        self.btn_maximum.move(btn_close_x - self.btn_maximum.width(), btn_close_y)
        self.btn_minimum.move(self.btn_maximum.x() - self.btn_minimum.width(), btn_close_y)
        return super(Window, self).resizeEvent(e)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.dragFlag = True
            self.current_pos = e.globalPos()
            self.current_widget_pos = self.pos()
        return super(Window, self).mousePressEvent(e)

    def mouseMoveEvent(self, e: QMouseEvent) -> None:
        if self.dragFlag:
            self.move(self.current_widget_pos + (self.cursor().pos() - self.current_pos))
        return super(Window, self).mouseMoveEvent(e)

    def mouseReleaseEvent(self, e: QMouseEvent) -> None:
        if e.button() == Qt.LeftButton:
            self.dragFlag = False
        return super(Window, self).mouseReleaseEvent(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

### 交互状态

#### 可用与显示

当一个窗口被绘制后，如果设置其中一个控件隐藏，实现的方式是从底层重新开始绘制一遍，注意一下即可。

```python
# 是否可用
.setEnable(bool)			# 设置控件是否禁用
.isEnable() -> bool			# 查看控件是否禁用
# 是否显示
.setVisible(bool)			# 设置控件是否可见，传递参数为 True 也未必可见
# .setVisible 衍生函数
.setHidden(bool)
.show()
.hide()			# 相对于父控件，也就是说父控件显示的情况下，当前控件是否被隐藏

.isHidden()
.isVisible()		# 即使被其他控件遮挡，也属于可见状态
.isVisibleTo(widget)	# 判断是否能跟着 widget 显示

.isActiveWindow()		# 是否为活跃窗口，并不是最上层的窗口才是活跃窗口
```

####  是否编辑

```python
.setWindowModified(bool)	# 设置被编辑状态 [*], []不会显示，set 为True时显示*，[]内只能放 *
.isWindowModified()			# 查看窗口是否是被编辑状态
```

#### 关闭

`.close()` 也可以隐藏控件。

但是开启属性后，就会释放掉控件：`.setAttribute(Qt.WA_DeleteOnClose, True)`

#### Example1

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/11 13:45"
"""

"""
Example：
创建一个窗口，包含一个文本框、按钮、标签
默认状态：标签隐藏，文本框和按钮显示，按钮设置为不可用状态
要求：1.当文本框有内容时，让按钮可用，否则不可用
     2.当文本框内容为 Jx 时，点击按钮则显示标签，且文本为登陆成功，否则为失败
"""

import sys
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("01_QWidget_Example7")
        self.resize(600, 400)
        # 首先创建所有需要的控件
        self.lineEdit = QLineEdit(self)
        self.btn = QPushButton(self)
        self.label = QLabel(self)
        self.setup_ui()

    def setup_ui(self):
        # 简单调整下布局
        self.lineEdit.resize(200, 25)
        self.lineEdit.move(10, 10)
        self.btn.resize(40, 25)
        self.btn.setText("登陆")
        self.btn.move(self.lineEdit.frameGeometry().topRight() + QPoint(10, 0))
        self.label.resize(100, 25)
        self.label.setStyleSheet("background-color: gray")
        self.label.move(self.lineEdit.frameGeometry().bottomLeft() + QPoint(0, 20))
        self.label.setAlignment(Qt.AlignCenter)
        # 默认状态
        self.label.setVisible(False)    # 标签隐藏
        self.btn.setEnabled(False)      # 按钮不可用
        # 实现要求
        self.lineEdit.textChanged.connect(self.textChangedEvent)
        self.btn.clicked.connect(self.btnClickedEvent)

    def textChangedEvent(self):
        self.btn.setEnabled(bool(self.sender().text()))
        self.label.setVisible(False)

    def btnClickedEvent(self):
        if self.lineEdit.text() == "Jx":
            self.label.setText("登陆成功")
        else:
            self.label.setText("登陆失败")
        self.label.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

### 信息提示

#### 状态栏

`MainWindow` 特有

```python
.setStatusTip(str)
.statisTip()

# 只有鼠标移动到调用对像上，才会设置状态栏
```

#### 信息提示

```python
.setToolTip(str)
.toolTip()
.setToolTipDuration(msec: int)		# 设置持续时长
```

#### 这是啥提示

窗口模式需要改变，才能显示 。`setWindowFlags(Qt.WindowContextHelpButtonHint)`

```python
.setWhatsThis(str)
.whatsThis()
```

### 焦点控制

控件的状态 称为 获取焦点 的状态。 常见的是点击一下。

#### 单个控件角度

```python
.setFocus()		# 指定控件获取焦点
.setFocusPolicy(Policy)		# 设置获取焦点策略
"""
Policy:
	Qt.TabFocus
	Qt.ClickFocus
	Qt.StrongFocus		tab或单击均可，默认策略
	Qt.NoFocus			tab或单击均不可
"""
.clearFocus()		# 取消焦点
```

#### 父控件角度

```python
.focusWidget()			# 获取子控件中当前聚焦的控件
.focusNextChild()		# 聚焦下一个子控件

```

#### TODO

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
|                        | 水平方向：`Qt.AlignLeft`,`Qt.AlignRight`,`Qt.AlignCenter`,`Qt.AlignJustify(两端对齐)` |
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

## 了解PyQt5库结构

查看模块父类 `QObject.mro()`

查看模块子类 `QObjcet.__subclasses__()`

### 常用模块

- QtWidgets

  包含了一整套UI元素控件，用于建立符合系统风格的界面

- QtGui

  涵盖了多种基本图形功能的类

  字体、图形、图标、颜色 ...

- QtCore

  涵盖了包的核心的非GUI功能

  时间、文件、目录、数据类型、

### 控件的创建

当我们创建一个控件后，如果说，这个控件没有父控件，则把它当做顶层控件（窗口），系统会自动的给窗口添加一些装饰（标题栏），窗口控件具备一些特性（设置标题，图标）

- 什么是控件

  一个程序界面上的各个独立的元素：一块矩形区域

  具备不同的功能：用户点击、接受用户输入、展示内容、存放其他控件

  常用控件：按钮、输入控件、展示控件、等等...

## QObject

***The base class of all Qt objects***

QObject是Qt对象模型的核心。这个模型的中心特性是一个非常强大的无缝对象通信机制，称为信号和插槽。可以使用connect()将信号连接到槽位，也可以使用disconnect()销毁连接。

### 方法解析顺序

```python
from PyQt5.Qt import *

mros = QObject.mro()    # Return a type's method resolution order.
for mro in mros:
    print(mro)
    
"""
<class 'PyQt5.QtCore.QObject'>
<class 'sip.wrapper'>
<class 'sip.simplewrapper'>
<class 'object'>	
"""
```

### 对象名称

```python
.setObjectName(str)	# 设置对象名
.objectName()		# 获取对象名，初始为空
```

### 对象属性

应用场景：用于qss的ID选择器，属性选择器，方便统一设置样式

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

- 获取 **dynamicPropertyNames()** 所有属性名称

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

- **findChild(参数1, 参数2, 参数3)**

参数1： 类型：QObject 等等

​			   类型元组：(QPushButton, QLabel) 等等

参数2：objectName ，可省略

参数3：查找选项：

​			Qt.FindChildrenRecursively	递归查找，默认选项

​			Qt.FindDirectChildrenOnly	只查找直接子对象

```python
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

        object1.setParent(object0)
        object2.setParent(object0)
        object3.setParent(object1)
        object4.setParent(object1)
        print(object0.findChild(QObject, "obj4").objectName())      # obj4
        print(object0.findChild(QObject, "obj4", Qt.FindChildrenRecursively).objectName())  # obj4
        print(object0.findChild(QObject, "obj4", Qt.FindDirectChildrenOnly))    # None
```

### 判断类型

```python
.isWidgetType(self) -> bool		# 判断是否为 Widget
.isWindowType(self) -> bool		# 判断是否为 Window
```

### 继承

```python
.inherits(self, str) -> bool	# 是否继承于某个类，包括直接或间接继承

obj = QObject()
print(obj.inherits('QPushButton'))    	# False
btn = QPushButton()
print(btn.inherits('QObject'))          # True
```

### 内置信号

#### 改变名称

```python
# 并不是 setObjectName() 就会触发函数，而是 Name 前后的确有变化了才会触发
.objectNameChanged(self, str) [signal]
```

**示例：**

```python
def func7(self):
    self.object.objectNameChanged.connect(lambda x: print("Name Changed", x))
    btn = QPushButton(self)
    # btn.clicked.connect(lambda: self.object.setObjectName("hello"))   # 这个只会接收一次
    btn.clicked.connect(lambda: self.object.setObjectName(f"{time.time()}"))    # 这个更好玩
```

#### 删除对象

```python
.destroyed(self, object: QObject = None) [signal]		# 被删除时释放信号
.deleteLater(self)		# 代码执行完后删除对象
# 并没有将对象立即销毁，而是向主消息循环发送了一个event，下一次主消息循环收到这个event之后才会销毁对象。
del [object]	# 只会删除标签，并不会删除对象本身内存
```

**示例：**

```python
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

# deleteLater() 函数是让带代码执行完毕后再释放，因此 object2 最后释放    
"""
object1被释放
object3被释放
object2被释放
"""
```

### 定时器

```python
timerEvent(self, QTimerEvent)		# 需要重载的函数
# 第一个参数是时间间隔(ms) 返回事件id
.startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int		
.killTimer(self, int)		# 停止时间事件，参数为事件id
```

**示例**：

```python
class JxObject(QObject):
    def timerEvent(self, QTimerEvent) -> None:
        print(QTimerEvent, time.time())
        
...
    def func6(self):
        btn = QPushButton(self)
        self.obj = JxObject()
        startId = self.obj.startTimer(1000)
        btn.pressed.connect(lambda: self.obj.killTimer(startId))
```

#### .startTimer()

```python
.startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int
# int: ms
# timerType:
'''Qt.PreciseTimer		精确定时器：尽可能保持毫秒准确
   Qt.CoarseTimer		粗定时器：5%的误差间隔
   Qt.VertCoarseTimer	很粗的定时器：只能到秒级'''
# return int: timer_id	定时器的唯一标识
```

## 事件、信号和槽

### 事件

信号与槽机制是对事件机制的高级封装，事件机制更偏底层。

在消息循环中，消息队列将事件包装成事件对象 `QEvent`,  然后发送给 `QApplication` 对象的 `notify(receiver, evt)` 方法。

#### 初次了解事件

重构 `notify()` 函数后，可以循环打印每次事件的接收者和对象。 

```python
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
        print(receiver, evt)
        # 不知道如何分发信号，就交给父类处理，注意要保持和父类同样的返回值
        return super().notify(receiver, evt)


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
        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)
        btn.clicked.connect(lambda: print("按钮被点击了"))


if __name__ == '__main__':
    app = App(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
```

- **筛选事件**

```python
class App(QApplication):
    def notify(self, receiver, evt) -> bool:
        # 先完成和父类相同的功能后，就可以打印出自己想查询的信息了
        if receiver.inherits("QPushButton") and evt.type() == QEvent.MouseButtonPress:
            print(receiver, evt)
        # 不知道如何分发信号，就交给父类处理，注意要保持和父类同样的返回值
        return super().notify(receiver, evt)
```

- **完整代码**

```python
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
```

#### 事件转发

事件转发：当事件发生时，就会发送事件，如果当前控件没有对事件进行处理，则会发送给 父控件 处理。

```python
evt.accept()		# 事件被接收，不会继续往父控件传递
evt.ignore()		# 事件被忽略，会继续向父控件传递
evt.isAccepted()	# 查看事件被接收的状态
```

### 信号与槽

信号分为控件内置的一些信号：`QPushButton().pressed` 、`QPushButton().clicked` 等；也可以自定义信号：`pyqtSignal()`。

语法：`object.信号.connect(槽函数)`

- **特性**

一个信号可以连接多个槽函数；

一个信号也可以连接另外一个信号；

信号的参数可以是任何Python类型；

一个槽可以监听多个信号；

···

#### API

```python
widget.信号.connect(槽)
obj.disconnect()			# 切断所有连接
widget.blockSignals(bool)	# bool=True 临时阻断连接
widget.signalsBlock()		# 获取信号是否被阻止
widget.receivers(信号)		# 获取连接信号的数量; 示例：参数=widget.pressed
```

- **案例1**

  每次在标题设置前，都加入前缀 `"Jx-"`

```python
"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/5/7 20:32"
"""

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
        def slotTitle(title):
            self.blockSignals(True)
            self.setWindowTitle("Jx-"+title)
            self.blockSignals(False)

        self.windowTitleChanged.connect(slotTitle)
        self.setWindowTitle("信号与槽案例")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个应用程序对象
    window = Window()
    window.show()
    sys.exit(app.exec_())  # 0是正常退出
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

#### .setContextMenuPolicy()

```python
.setContextMenuPolicy(self, Qt.ContextMenuPolicy)	# 允许右键产生子菜单、
.customContextMenuRequested(self, QPoint) [signal]	# 自定义菜单请求


# example
.setContextMenuPolicy(Qt.CustomContextMenu)		# 设置自定义菜单
.customContextMenuRequested.connect(self.tableWidget_menu)		# 连接自定义菜单
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

