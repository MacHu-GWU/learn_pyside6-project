# -*- coding: utf-8 -*-

"""
这是一个用于演示对于拥有自己一套 layout 的子 widget, 在父 widget 中什么时候应该用 addWidget,
什么时候应该用 addLayout 的演示. 这个例子要用
``sub_widget_and_sub_layout_1_1.py`` 和 ``sub_widget_and_sub_layout_1_2.py``
一起比较来看才能看出区别.

这个例子是在子 widget 不使用 setLayout 方法, 而只是定义子 widget 中的 main_layout 的定义,
然后再然后在父 widget 中使用 addLayout 方法添加子 widget 的 layout 到父 widget 的 layout 中.

结论, 子 widget 有一个隐形的方框, 由于这里没有用子 widget, 而是直接将子 widget 中的 子 widget
的元素加到总的 layout 中取, 所以看起来离外面的边框近一点.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QMainWindow,
)
from PySide6 import QtWidgets
import sys


class LabelListWidget(QWidget):
    def __init__(self, parent, ith: int):
        super().__init__(parent)
        self.ith = ith

        self.main_layout = QVBoxLayout()

        for j in range(1, 1 + 3):
            label_wgt = QLabel(f"Label {self.ith}-{j}", parent=parent)
            self.main_layout.addWidget(label_wgt)


class MainWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.label_list_1 = LabelListWidget(self, ith=1)
        self.main_lay = QVBoxLayout()
        self.main_lay.addLayout(self.label_list_1.main_layout)
        self.setLayout(self.main_lay)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_wgt = MainWidget(self)
        self.main_wgt.setStyleSheet("Border: 1px solid black;")
        self.setCentralWidget(self.main_wgt)
        self.setWindowTitle("Sub Widget and Sub Layout Example 1-2")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())
