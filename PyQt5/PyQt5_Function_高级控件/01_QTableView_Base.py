from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Page242
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

