# -*- coding: utf-8 -*-

"""
这个例子把三个 QScrollArea Widget 叠加到一起, 两个 widget 嵌入在一个 widget 中.
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
    def create_inner_scroll_area_wgt(self, ith: int) -> QScrollArea:
        """
        Create a scroll area widget with a collection of label widget.
        """
        inner_scroll_area_wgt = QScrollArea()
        inner_scroll_area_wgt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        inner_scroll_area_wgt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        inner_scroll_area_wgt.setMaximumHeight(400)

        inner_area_content_wgt = QWidget()
        list_of_label_wgt = list()
        n = 50
        for i in range(1, 1 + n):
            label_wgt = QLabel(f"Inner Scroll Area Label {ith} - {i}")
            list_of_label_wgt.append(label_wgt)

        # The Vertical Box that contains the collection of label widget
        inner_area_content_wgt_lay = QVBoxLayout()
        for label_wgt in list_of_label_wgt:
            inner_area_content_wgt_lay.addWidget(label_wgt)
        inner_area_content_wgt.setLayout(inner_area_content_wgt_lay)

        # The scroll area only contains one widget, which is the "inner_area_content_wgt"
        inner_scroll_area_wgt.setWidget(inner_area_content_wgt)

        return inner_scroll_area_wgt

    def __init__(self):
        super().__init__()
        # ----------------------------------------------------------------------
        # declare widgets
        # ----------------------------------------------------------------------
        self.inner_scroll_area_wgt_1 = self.create_inner_scroll_area_wgt(1)
        self.inner_scroll_area_wgt_2 = self.create_inner_scroll_area_wgt(2)

        self.outer_scroll_area_wgt = QScrollArea()
        self.outer_scroll_area_wgt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.outer_scroll_area_wgt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.outer_scroll_area_wgt.setMaximumHeight(600)

        self.outer_scroll_area_content_wgt = QWidget()
        self.outer_scroll_area_content_wgt_lay = QVBoxLayout()
        self.outer_scroll_area_content_wgt_lay.addWidget(self.inner_scroll_area_wgt_1)
        self.outer_scroll_area_content_wgt_lay.addWidget(self.inner_scroll_area_wgt_2)

        self.outer_scroll_area_content_wgt.setLayout(self.outer_scroll_area_content_wgt_lay)

        self.outer_scroll_area_wgt.setWidget(self.outer_scroll_area_content_wgt)
        # ----------------------------------------------------------------------
        # Set Window
        # ----------------------------------------------------------------------
        # The set the "main_wgt_scroll_area" as central widget in App window
        self.setCentralWidget(self.outer_scroll_area_wgt)

        # Set window property
        self.setGeometry(
            int(screen_width * 0.25),  # x, at 25% of screen width
            int(screen_height * 0.25),  # y, at 25% of screen height
            int(screen_width * 0.5),  # w, 50% screen width
            int(screen_height * 0.5),  # h, 50% screen height
        )
        self.setWindowTitle("Nested Scroll Area Demonstration")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
