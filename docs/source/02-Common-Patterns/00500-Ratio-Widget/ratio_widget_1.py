# -*- coding: utf-8 -*-

"""
演示如何使用 ratio. 并且演示了如何正确使用 ``QRadioButton.toggled`` 的 signal.
"""

import sys
from PySide6 import QtCore, QtWidgets


class MainWidget(QtWidgets.QWidget):
    """
    Ref:

    - QRadioButton: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html
    - QButtonGroup: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QButtonGroup.html
    """

    def __init__(self, parent):
        super().__init__(parent)
        # define
        # 在一个 parent 下的所有 Radio, 默认情况下都是 exclusive 的, 即只能有一个被选中.
        # 如果你需要让在一个 parent 下的 Ratio 分组, 通常有两种做法:
        # 1. 把他们放到另一个 widget 中
        # 2. 使用 QButtonGroup
        self.ratio_1_wgt = QtWidgets.QRadioButton("label 1-1", self)
        self.ratio_1_wgt.toggled.connect(self.on_ratio_toggled_handler)
        self.ratio_2_wgt = QtWidgets.QRadioButton("label 1-2", self)
        self.ratio_2_wgt.toggled.connect(self.on_ratio_toggled_handler)

        self.main_lay = QtWidgets.QHBoxLayout()  # Vertical Box layout
        self.main_lay.addWidget(self.ratio_1_wgt)
        self.main_lay.addWidget(self.ratio_2_wgt)
        self.setLayout(self.main_lay)

    @QtCore.Slot()
    def on_ratio_toggled_handler(self):
        """
        在定义 check / uncheck 的 signal 的时候, 这里有个问题是你需要所有的 Radio 都有一个 signal
        这会导致多次重复触发的问题. 因为你选择一个 ratio 的时候, 其他的 ratio 也会自动改变状态,
        等于是所有 ratio 的 toggler 都触发了 signal, 这是不必要的. 正确的做法是先判断当前的
        ratio button 是不是 checked, 如果不是 checked 就不要执行后面的逻辑.
        """
        radio_button: QtWidgets.QRadioButton = self.sender()
        if radio_button.isChecked():
            print(
                f"{self.ratio_1_wgt.isChecked() = }, {self.ratio_2_wgt.isChecked() = }"
            )


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
