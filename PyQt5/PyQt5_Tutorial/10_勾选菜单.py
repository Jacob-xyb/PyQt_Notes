import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()       # 创建一个状态栏对象
        self.statusbar.showMessage('Ready')     # 状态栏显示 ‘Ready’
        menubar = self.menuBar()                # 返回一个菜单栏对象
        viewMenu = menubar.addMenu('View')      # addMenu(self, str) -> QMenu 菜单对象
        # 用 checkable 选项创建一个能选中的菜单。
        viewStatAct = QAction('View statusbar', self, checkable=True)       # 创建一个动作
        viewStatAct.setStatusTip('View statusbar')
        # 默认设置为选中状态。
        viewStatAct.setChecked(True)
        # 依据选中状态切换状态栏的显示与否。
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())