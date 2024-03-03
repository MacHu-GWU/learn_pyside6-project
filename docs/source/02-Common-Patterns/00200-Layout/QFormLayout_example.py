# -*- coding: utf-8 -*-

"""
QFormLayout Example.
"""

import sys
from PySide6 import QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        main_lay_form = QtWidgets.QFormLayout(self)

        main_lay_form.addRow(QtWidgets.QLabel("Firstname"), QtWidgets.QLineEdit())
        main_lay_form.addRow(QtWidgets.QLabel("Lastname"), QtWidgets.QLineEdit())

        age_input_box_wgt = QtWidgets.QSpinBox()
        age_input_box_wgt.setMinimumWidth(
            100,  # minw
        )
        main_lay_form.addRow(QtWidgets.QLabel("Age"), age_input_box_wgt)

        self.setLayout(main_lay_form)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_wgt = MainWidget(self)
        self.setCentralWidget(self.main_wgt)
        self.setGeometry(
            int(screen_width * 0.25),  # x
            int(screen_height * 0.25),  # y
            int(screen_width * 0.5),  # w
            int(screen_height * 0.5),  # h
        )
        self.setWindowTitle("QFormLayout_example")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
