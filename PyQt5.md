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

# 控件描述

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



# PyQt5_Tutorial

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

