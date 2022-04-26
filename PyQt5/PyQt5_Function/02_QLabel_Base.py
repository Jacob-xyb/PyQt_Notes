# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap


class WinForm(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.initUI()
        self.init_label()

        # 基本参数
        print("QLabel().sizeHint(): ", QLabel().sizeHint())
        print("QLabel().minimumSizeHint(): ", QLabel().minimumSizeHint())

    def initUI(self):
        self.setWindowTitle("QLabel_Base")
        self.setGeometry(600, 500, 400, 300)

    def init_label(self):
        # == set label1
        self.label1.setText("this is text label.")
        self.label1.setAlignment(Qt.AlignCenter)
        # 开启填充背景，才能上色
        self.label1.setAutoFillBackground(True)
        # 调色板
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)
        self.label1.setPalette(palette)
        # ===============
        # == set label2
        self.label2.setText("<a href='#'>欢迎使用 Python GUI 应用</a>")
        self.label2.setAlignment(Qt.AlignCenter)
        # ===============
        # == set label3
        # 提示气泡
        self.label3.setToolTip('这是一个图片标签')
        self.label3.setAlignment(Qt.AlignCenter)
        # label 变 图片
        self.label3.setPixmap(QPixmap("../../image/Globe.png"))
        # ===============
        # == set label4
        self.label4.setText("<a href='https://blog.csdn.net/weixin_44560698?spm=1010.2135.3001.5343'>欢迎访问Jx的小书屋</a>")
        self.label4.setAlignment(Qt.AlignRight)
        # 打开允许访问超链接，默认是不允许
        self.label4.setOpenExternalLinks(True)
        # == 布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)
        self.setLayout(vbox)

        # == set 事件
        self.label1.linkActivated.connect(self.link_clicked)
        self.label2.linkActivated.connect(self.link_clicked)
        self.label2.linkHovered.connect(self.link_hovered)
        self.label4.linkActivated.connect(self.link_clicked)

    def link_clicked(self):
        if self.sender() == self.label4:
            print("欢迎来到我的小屋.")
        elif self.sender() == self.label1:
            # label 1 不带超链接 所以无法生效
            print("点击了 label1")
        elif self.sender() == self.label2:
            print("点击了 label2")

    def link_hovered(self):
        print("鼠标滑过了label2..")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WinForm()
    w.show()
    sys.exit(app.exec_())
