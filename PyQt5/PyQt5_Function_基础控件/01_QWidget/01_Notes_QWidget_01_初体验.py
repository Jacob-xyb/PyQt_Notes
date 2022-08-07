"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2022/8/6 11:03"
"""

from PyQt5.Qt import *
import sys

print(sys.argv)     # 系统输入参数列表

app = QApplication(sys.argv)        # 创建一个应用程序
print(app.arguments())      # 和 sys.argv 是一致的
print(qApp.arguments())     # qApp  是一个全局变量，可以用来直接获取参数

window = QWidget()      # 创建控件对象
window.setWindowTitle("QWidget 初体验")        # 设置标题栏
window.resize(500, 500)     # 设置尺寸
window.move(400, 200)       # 设置初始位置

label = QLabel(window)      # 创建 Label
label.setText("Hello World")   # 设置内容
label.setAccessibleName("Hello Jx")     # 会掩盖掉 Inspect 中的属性
label.move(200, 200)

window.show()
# sys.exit(status)  # 传入一个状态 退出码 0 为正常
sys.exit(app.exec_())       # 开始执行一个应用程序，并进入消息循环
