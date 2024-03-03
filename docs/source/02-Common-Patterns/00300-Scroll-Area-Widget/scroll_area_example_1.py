# -*- coding: utf-8 -*-

"""
这是一个用于演示如何使用 ``QScrollArea`` 来创建一个内容很长, 需要用滚动区域来限制大小的例子.
在这个例子中我们的 App 只有一个 ``QScrollArea`` Widget, 里面包含了一堆 ``QLabel`` Widget.
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QMainWindow,
)
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ----------------------------------------------------------------------
        # declare widgets
        # ----------------------------------------------------------------------
        # Scroll Area which contains the widgets, set as the centralWidget
        self.main_wgt_scroll_area = QScrollArea()
        self.main_wgt_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.main_wgt_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_wgt_scroll_area.setWidgetResizable(True)

        self.list_of_label_wgt = list()
        n = 50
        for i in range(1, 1 + n):
            label_wgt = QLabel(f"TextLabel {i}")
            self.list_of_label_wgt.append(label_wgt)

        # Widget that contains the collection of label widget
        self.label_list_wgt = QWidget()

        # ----------------------------------------------------------------------
        # declare layouts
        # ----------------------------------------------------------------------
        # The Vertical Box that contains the collection of label widget
        self.label_list_wgt_lay = QVBoxLayout()
        for label_wgt in self.list_of_label_wgt:
            self.label_list_wgt_lay.addWidget(label_wgt)
        self.label_list_wgt.setLayout(self.label_list_wgt_lay)

        # The scroll area only contains one widget, which is the "label_list_wgt"
        self.main_wgt_scroll_area.setWidget(self.label_list_wgt)

        # ----------------------------------------------------------------------
        # Set Window
        # ----------------------------------------------------------------------
        # The set the "main_wgt_scroll_area" as central widget in App window
        self.setCentralWidget(self.main_wgt_scroll_area)

        # Set window property
        self.setGeometry(
            int(screen_width * 0.25),  # x, at 25% of screen width
            int(screen_height * 0.25),  # y, at 25% of screen height
            int(screen_width * 0.5),  # w, 50% screen width
            int(screen_height * 0.5),  # h, 50% screen height
        )
        self.setWindowTitle("Scroll Area Demonstration")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
