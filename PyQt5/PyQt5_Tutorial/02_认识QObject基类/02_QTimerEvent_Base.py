__author__ = "Jacob-xyb"

import sys
import time
from PyQt5.Qt import *

class JxObject(QObject):
    def timerEvent(self, QTimerEvent) -> None:
        print(QTimerEvent, time.time())


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("")
window.resize(600, 400)
btn = QPushButton(window)
obj = JxObject()
startId = obj.startTimer(1000)
btn.pressed.connect(lambda: obj.killTimer(startId))
# 2.3 展示控件
window.show()

# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec_())
