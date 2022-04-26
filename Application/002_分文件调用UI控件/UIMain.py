import sys
from Widget1 import Ui_Form1
from Widget2 import Ui_Form2
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QHBoxLayout
from PyQt5 import QtCore


class MyMainForm(QWidget):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.resize(600, 400)
        self.widget1 = QWidget(self)
        Ui_Form1().setupUi(self.widget1)
        self.widget2 = QWidget(self)
        Ui_Form2().setupUi(self.widget2)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.widget1)
        self.hbox.addWidget(self.widget2)
        self.setLayout(self.hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())



