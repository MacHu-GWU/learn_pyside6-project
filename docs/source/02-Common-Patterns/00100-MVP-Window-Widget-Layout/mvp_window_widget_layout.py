# -*- coding: utf-8 -*-

"""
一个最简单的 GUI App 的代码框架, 至少包含一个 MainWindow 和一个 MainWidget 类.

知识点:

- 用 ``${name}_wgt`` 表示 widget.
- 用 ``${name}_lay`` 表示 layout.
- 用 ``main_wgt`` 表示主要的 widget, 也就是最外层的 widget.
- 用 ``main_lay`` 表示主要的 layout, 也就是最外层的 layout.
- 用 ``QtWidgets.QApplication().screen()[0].size().toTuple()`` 来获取屏幕的大小, 以便于设置窗口的位置和大小.
"""

import sys
from PySide6 import QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        # define
        self.label_wgt = QtWidgets.QLabel("This is a Label")
        self.main_lay = QtWidgets.QVBoxLayout()  # Vertical Box layout
        self.main_lay.addWidget(self.label_wgt)
        self.setLayout(self.main_lay)


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
        self.setWindowTitle("mvp_window_widget_layout")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
