# -*- coding: utf-8 -*-

"""
演示如何对 ratio button 进行分组, 使得在一个组内, 最多只能有一个 ratio button 可以被 check.
你在 App 中可以看到, label 1-1 和 label 1-2 是一组, label 2-1 和 label 2-2 是一组.
"""

import sys
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    """
    Reference:

    - QRadioButton: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html
    - QButtonGroup: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QButtonGroup.html
    """

    def __init__(self, parent):
        super().__init__(parent)
        # Define button group
        # 注意 ``QButtonGroup`` 不是一个 widget, 它只是一个 container, 可以将里面的
        self.button_group_1 = QtWidgets.QButtonGroup(self)
        self.ratio_1_1_wgt = QtWidgets.QRadioButton("label 1-1", self)
        self.ratio_1_1_wgt.toggled.connect(self.button_group_1_toggled_handler)
        self.button_group_1.addButton(self.ratio_1_1_wgt)
        self.ratio_1_2_wgt = QtWidgets.QRadioButton("label 1-2", self)
        self.ratio_1_2_wgt.toggled.connect(self.button_group_1_toggled_handler)
        self.button_group_1.addButton(self.ratio_1_2_wgt)

        self.button_group_2 = QtWidgets.QButtonGroup(self)
        self.ratio_2_1_wgt = QtWidgets.QRadioButton("label 2-1", self)
        self.ratio_2_1_wgt.toggled.connect(self.button_group_2_toggled_handler)
        self.button_group_2.addButton(self.ratio_2_1_wgt)
        self.ratio_2_2_wgt = QtWidgets.QRadioButton("label 2-2", self)
        self.ratio_2_2_wgt.toggled.connect(self.button_group_2_toggled_handler)
        self.button_group_2.addButton(self.ratio_2_2_wgt)

        self.main_lay = QtWidgets.QVBoxLayout()  # Vertical Box layout

        self.button_group_1_lay = QtWidgets.QHBoxLayout()  # Horizontal Box layout
        self.button_group_1_lay.addWidget(self.ratio_1_1_wgt)
        self.button_group_1_lay.addWidget(self.ratio_1_2_wgt)
        self.main_lay.addLayout(self.button_group_1_lay)

        self.button_group_2_lay = QtWidgets.QHBoxLayout()  # Horizontal Box layout
        self.button_group_2_lay.addWidget(self.ratio_2_1_wgt)
        self.button_group_2_lay.addWidget(self.ratio_2_2_wgt)
        self.main_lay.addLayout(self.button_group_2_lay)

        self.setLayout(self.main_lay)

    def print_radio_button_status(self):
        print(
            f"label 1-1 = {self.ratio_1_1_wgt.isChecked()}, "
            f"label 1-2 = {self.ratio_1_2_wgt.isChecked()}, "
            f"label 2-1 = {self.ratio_2_1_wgt.isChecked()}, "
            f"label 2-2 = {self.ratio_2_2_wgt.isChecked()}"
        )

    @QtCore.Slot()
    def button_group_1_toggled_handler(self):
        radio_button: QtWidgets.QRadioButton = self.sender()
        if radio_button.isChecked():
            self.print_radio_button_status()

    @QtCore.Slot()
    def button_group_2_toggled_handler(self):
        radio_button: QtWidgets.QRadioButton = self.sender()
        if radio_button.isChecked():
            self.print_radio_button_status()


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
