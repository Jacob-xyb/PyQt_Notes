import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        q_icon = QIcon('..\\..\\image\\Globe.ico')
        # QAction是菜单栏、工具栏或者快捷键的动作的组合。前面两行，我们创建了一个图标、一个exit的标签和一个快捷键组合，都执行了一个动作。
        # 第三行，创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct = QAction(q_icon, '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # qApp = QApplication()
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
