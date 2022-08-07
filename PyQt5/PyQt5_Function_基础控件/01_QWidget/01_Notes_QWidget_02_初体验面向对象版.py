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
        self.setWindowTitle("QWidget 初体验")  # 设置标题栏
        self.resize(500, 500)  # 设置尺寸
        # self.move(400, 200)  # 设置初始位置
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)      # 创建 Label
        label.setText("Hello World")   # 设置内容
        label.move(200, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    choose = 1
    if choose == 0:     # 如果封装成一个类，就可以用 setParent() 来设置父类，但是设置父类后，此控件就不能单独显示了
        main_window = QMainWindow()
        main_window.resize(600, 400)
        window = MainWindow()
        window.setParent(main_window)
        main_window.show()
    elif choose == 1:
        window = MainWindow()
        window.show()
    sys.exit(app.exec_())       # 开始执行一个应用程序，并进入消息循环
