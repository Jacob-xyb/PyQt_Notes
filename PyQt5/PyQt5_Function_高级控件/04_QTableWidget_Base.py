from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QHeaderView, QAbstractItemView
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
        self.tableWidget.setHorizontalHeaderLabels(self.HeaderLabels)   # 应该在行列设置后，不然不显示
        self.tableWidget.setVerticalHeaderLabels(['a', 'b', 'c', 'd'])
        # 用 QTableWidgetItem 装填数据
        for row in range(4):
            for col in range(len(self.HeaderLabels)):
                # QTableWidget 必须用自己的 Item 装填数据， setModel() 变为了私有方法
                item = QTableWidgetItem("row %s, col %s" % (row, col))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)    # 可以设置居中之类的
                self.tableWidget.setItem(row, col, item)
        # self.tableWidget.clear()            # 清除所有数据包括行列
        # self.tableWidget.clearContents()      # 清除所有数据不包括行列

        self.tableWidget.setColumnWidth()

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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())

