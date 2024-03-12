# -*- coding: utf-8 -*-

"""
"""

import sys
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    """
    Ref:

    - QLabel: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html
    """

    def __init__(self, parent):
        super().__init__(parent)
        # fmt: off
        # define
        # 这是最基本的定义一个 Label 的语法
        # 你还可以设置其最大宽度, 对齐方式等.
        self.line_edit_1_wgt = QtWidgets.QLineEdit(self)
        self.line_edit_1_wgt.setPlaceholderText("Enter something here")

        self.line_edit_2_wgt = QtWidgets.QLineEdit(self)
        self.line_edit_2_wgt.setText("This is read only text")
        self.line_edit_2_wgt.setReadOnly(True)

        self.line_edit_3_wgt = QtWidgets.QLineEdit(self)
        self.line_edit_3_wgt.setPlaceholderText("Type here will trigger a event")
        self.line_edit_3_wgt.textEdited

        # # 默认情况下 label 是可以是 HTML 的. 你可以放一个 <a> tag 用于实现一个超链接
        # # 当然你还可以用 HTML 来实现颜色, style 等等.
        # # 你需要 connect ``linkActivated`` signal 来处理点击事件, 决定用户点击链接的时候
        # # 会发生什么.
        # self.label_2_wgt = QtWidgets.QLabel("<font color='red'>label 2</font>: <a href='https://www.google.com'>Click here to visit Google</a>", self)
        # self.label_2_wgt.linkActivated.connect(self.label_2_link_activated_handler)
        #
        # # 当然我们默认情况下都是希望用户点击链接后就在浏览器中打开, 那么你可以
        # # 调用 ``setOpenExternalLinks(True)`` 来将其设为可以通过点击打开链接.
        # # 这等于是 QT 帮你实现了这个 signal, 你就无需自己实现了.
        # self.label_3_wgt = QtWidgets.QLabel("<font color='green'>label 3</font>: <a href='https://www.google.com'>Click here to visit Google</a>", self)
        # self.label_3_wgt.setOpenExternalLinks(True)
        # fmt: on

        self.main_lay = QtWidgets.QVBoxLayout()  # Vertical Box layout
        self.main_lay.addWidget(self.line_edit_1_wgt)
        self.main_lay.addWidget(self.line_edit_2_wgt)
        # self.main_lay.addWidget(self.label_3_wgt)
        self.setLayout(self.main_lay)

    @QtCore.Slot()
    def label_2_link_activated_handler(self):
        print("trigger label_2_link_activated_handler")


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
        self.setWindowTitle("ratio_widget")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
