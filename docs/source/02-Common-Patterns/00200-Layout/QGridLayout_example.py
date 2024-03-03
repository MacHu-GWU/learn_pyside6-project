# -*- coding: utf-8 -*-

"""
QGridLayout Example.
"""

import sys
from PySide6 import QtWidgets


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        button1_wgt = QtWidgets.QPushButton("One")
        button2_wgt = QtWidgets.QPushButton("Two")
        button3_wgt = QtWidgets.QPushButton("Three")
        button4_wgt = QtWidgets.QPushButton("Four")
        button5_wgt = QtWidgets.QPushButton("Five")

        main_lay = QtWidgets.QGridLayout(self)
        main_lay.addWidget(button1_wgt, 0, 0)
        main_lay.addWidget(button2_wgt, 0, 1)
        main_lay.addWidget(
            button3_wgt,
            1,  # row, start from 0
            0,  # column, start from 0
            1,  # rowSpan
            2,  # columnSpan
        )
        main_lay.addWidget(button4_wgt, 2, 0)
        main_lay.addWidget(button5_wgt, 2, 1)

        self.setLayout(main_lay)


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
        self.setWindowTitle("QGridLayout_example")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
