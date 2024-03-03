# -*- coding: utf-8 -*-

"""
这个例子基于前一个例子, 演示了如何把 ScrollArea 和其他的 widget 结合起来放在一起.
在这个例子中, 我们在 QScrollArea Widget 的上面和下面分别放了一个 QLabel Widget,
并且设定只有 QScrollArea 能够滚动.
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
        # --- before scroll area
        self.before_scroll_area_wgt_list = list()
        for i in range(1, 1+10):
            label_wgt = QLabel(f"Before {i}")
            self.before_scroll_area_wgt_list.append(label_wgt)

        # --- scroll area related widgets ---
        # Scroll Area which contains the widgets, set as the centralWidget
        self.scroll_area_wgt = QScrollArea()
        self.scroll_area_wgt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area_wgt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area_wgt.setMaximumHeight(200)
        self.scroll_area_wgt.setWidgetResizable(True)

        self.list_of_label_wgt = list()
        n = 50
        for i in range(1, 1 + n):
            label_wgt = QLabel(f"TextLabel {i}")
            self.list_of_label_wgt.append(label_wgt)

        # Widget that contains the collection of label widget
        self.label_list_wgt = QWidget()

        # --- after scroll area
        self.after_scroll_area_wgt_list = list()
        for i in range(1, 1 + 10):
            label_wgt = QLabel(f"After {i}")
            self.after_scroll_area_wgt_list.append(label_wgt)

        self.main_wgt = QWidget()
        # ----------------------------------------------------------------------
        # declare layouts
        # ----------------------------------------------------------------------
        # The Vertical Box that contains the collection of label widget
        self.label_list_wgt_lay = QVBoxLayout()
        for label_wgt in self.list_of_label_wgt:
            self.label_list_wgt_lay.addWidget(label_wgt)
        self.label_list_wgt.setLayout(self.label_list_wgt_lay)

        # The scroll area only contains one widget, which is the "label_list_wgt"
        self.scroll_area_wgt.setWidget(self.label_list_wgt)

        self.main_lay = QVBoxLayout()

        # many label widget before scroll area widget
        for label_wgt in self.before_scroll_area_wgt_list:
            self.main_lay.addWidget(label_wgt)

        # scroll area widget
        self.main_lay.addWidget(self.scroll_area_wgt)

        # many label widget after scroll area widget
        for label_wgt in self.after_scroll_area_wgt_list:
            self.main_lay.addWidget(label_wgt)

        self.main_wgt.setLayout(self.main_lay)

        # ----------------------------------------------------------------------
        # Set Window
        # ----------------------------------------------------------------------
        # The set the "main_wgt_scroll_area" as central widget in App window
        self.setCentralWidget(self.main_wgt)

        # Set window property
        self.setGeometry(
            int(screen_width * 0.25),  # x, at 25% of screen width
            int(screen_height * 0.25),  # y, at 25% of screen height
            int(screen_width * 0.5),  # w, 50% screen width
            int(screen_height * 0.5),  # h, 50% screen height
        )
        self.setWindowTitle("Scroll Area and other widgets Demonstration")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
