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
