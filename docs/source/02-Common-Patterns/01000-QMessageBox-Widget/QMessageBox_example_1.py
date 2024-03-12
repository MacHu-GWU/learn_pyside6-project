# -*- coding: utf-8 -*-

"""
这个例子展示了一个简单的 QMessageBox 的用法. 重点是展示了 exec, open, show 三种不同的方法来显示 QMessageBox.
"""

import sys
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # fmt: off
        self.button_wgt_1 = QtWidgets.QPushButton("Button 1", parent=self)
        self.button_wgt_1.clicked.connect(self.button_1_clicked_handler)
        self.button_wgt_2 = QtWidgets.QPushButton("Button 2", parent=self)
        self.button_wgt_2.clicked.connect(self.button_2_clicked_handler)
        self.button_wgt_3 = QtWidgets.QPushButton("Button 3", parent=self)
        self.button_wgt_3.clicked.connect(self.button_3_clicked_handler)

        # ref: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html
        self.msg_box_1 = QtWidgets.QMessageBox(parent=self)
        self.msg_box_1.setText("This is message box 1")
        self.msg_box_2 = QtWidgets.QMessageBox(parent=self)
        self.msg_box_2.setText("This is message box 2")
        self.msg_box_3 = QtWidgets.QMessageBox(parent=self)
        self.msg_box_3.setText("This is message box 3")
        # fmt: on

        self.main_lay = QtWidgets.QHBoxLayout()
        self.main_lay.addWidget(self.button_wgt_1)
        self.main_lay.addWidget(self.button_wgt_2)
        self.main_lay.addWidget(self.button_wgt_3)
        self.setLayout(self.main_lay)

    @QtCore.Slot()
    def button_1_clicked_handler(self):
        """
        exec() 方法会阻塞程序, 你不点 OK 是不会运行 print("msg box 1 exec() finished") 的.
        这是 QDialog 的方法. 所有的 QDialog 都有这个方法. 我们比较推荐使用这个方法.

        该方法默认会阻止用户和其他窗口互动.
        """
        print("trigger button_1_clicked_handler")
        # ref: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialog.html#PySide6.QtWidgets.PySide6.QtWidgets.QDialog.exec
        self.msg_box_1.exec()
        print("msg box 1 exec() finished")

    @QtCore.Slot()
    def button_2_clicked_handler(self):
        """
        open() 不会阻塞程序. 你会看到你点击 OK 之前 print("msg box 2 open() finished") 就
        已经被执行了. 其他方面和 exec() 完全一致.

        该方法默认会阻止用户和其他窗口互动.
        """
        print("trigger button_2_clicked_handler")
        # ref: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMessageBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QMessageBox.open
        self.msg_box_2.open()
        print("msg box 2 open() finished")

    @QtCore.Slot()
    def button_3_clicked_handler(self):
        """
        show() 不会阻塞程序. 你会看到你点击 OK 之前 print("msg box 2 open() finished") 就
        已经被执行了. show 本质上只是显示 widget, 只不过我们的 widget 恰巧是一个 QMessageBox.
        show 方法不会触发 MessageBox 的一些例如 finished(), buttonClicked() 的信号.
        它只适用于点击 OK 关闭窗口 (我知道了) 的情况.

        该方法默认会阻止用户和其他窗口互动.
        """
        print("trigger button_3_clicked_handler")
        # ref: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.show
        self.msg_box_3.show()
        print("msg box 3 show() finished")


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
