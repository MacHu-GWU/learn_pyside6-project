# -*- coding: utf-8 -*-

"""
这个例子展示了如何让 QMessageBox 里出现几个 button 选项, 点击不同的选项就会有不同的效果.
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
        self.msg_box.setText("This is a message box")
        self.msg_box.setStandardButtons(
            QtWidgets.QMessageBox.StandardButton.Save
            | QtWidgets.QMessageBox.StandardButton.Discard
            | QtWidgets.QMessageBox.StandardButton.Cancel
        )
        # fmt: on

        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.addWidget(self.button_wgt)
        self.setLayout(self.main_lay)

    @QtCore.Slot()
    def button_clicked_handler(self):
        """
        如果你要根据用户在 Message box 里点击的按钮来做不同的事情, 你需要用 ``exec`` 方法来
        阻塞程序, 并获得反馈后才继续执行.

        ``QtWidgets.QMessageBox.StandardButton`` 是一个 enum, 里面有很多预先定义好的
        button, 非常实用.
        """
        print("trigger button_clicked_handler")
        received = self.msg_box.exec()
        if received == QtWidgets.QMessageBox.StandardButton.Save:
            print("user clicked Save")
        elif received == QtWidgets.QMessageBox.StandardButton.Discard:
            print("user clicked Discard")
        elif received == QtWidgets.QMessageBox.StandardButton.Cancel:
            print("user clicked Cancel")
        else:  # pragma: no cover
            raise NotImplementedError


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
