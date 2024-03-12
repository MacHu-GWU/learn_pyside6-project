# -*- coding: utf-8 -*-

"""
这个例子展示了如何自动关闭 QMessageBox.
"""

import sys
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # fmt: off
        self.button_wgt = QtWidgets.QPushButton("Click Me", parent=self)
        self.button_wgt.clicked.connect(self.button_clicked_handler)
        # ref: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html
        self.msg_box = QtWidgets.QMessageBox(parent=self)
        self.msg_box.setText("This is a message box, will close in 3 seconds")
        # fmt: on

        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.button_wgt)
        self.setLayout(self.main_lay)

    @QtCore.Slot()
    def button_clicked_handler(self):
        """
        注意, 这个 timer 可一定不要放在 __init__ 中. 因为 QtCore.QTimer() 一初始化,
        就开始计时了. 你放在 __init__ 就会导致这个 gui 第一次显示后 3 秒就自动关闭 message box.
        这时候用户可能还没有点击 button, 还没有打开呢, 你之后再点击 button 的时候, 自然也不会自动关闭了.
        """
        print("trigger button_clicked_handler")
        timer = QtCore.QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(self.msg_box.close)
        timer.start(3000)  # 1000 milliseconds = 1 second
        self.msg_box.exec()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_wgt = MainWidget(self)
        self.setCentralWidget(self.main_wgt)
        self.setGeometry(
            int(screen_width * 0.25),  # x, at 25% of screen width
            int(screen_height * 0.25),  # y, at 25% of screen height
            int(screen_width * 0.5),  # w, 50% screen width
            int(screen_height * 0.5),  # h, 50% screen height
        )
        self.setWindowTitle("QMessageBox Example")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
