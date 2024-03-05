# -*- coding: utf-8 -*-

"""
这是一个用于演示如何使用 ``QScrollArea`` 来创建一个可以滚动的区域的例子.

在这个例子中我们的 App 的主窗口中只有一个 ``QScrollArea`` (scroll_area_wgt) Widget.
里面必须包含有且只有一个作为容器的 ``QWidget`` (scroll_area_content_wgt). 所有你想要放在
Scroll Area 中的 widget 都需要被添加到 scroll_area_content_wgt 的 Layout 中. 注意,
不是直接添加到 scroll_area_wgt 中. 最后调用 ``scroll_area_wgt.setWidget(scroll_area_content_wgt)``
方法将 scroll_area_content_wgt 作为唯一的 widget 添加到 scroll_area_wgt 中既可.

Reference:

- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QScrollArea.html
"""

from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a widget as a container for all other widgets in the scroll area
        self.scroll_area_content_wgt = QtWidgets.QWidget(self)
        self.scroll_area_content_wgt_lay = QtWidgets.QVBoxLayout()
        # add lots of widgets to the scroll area content widget
        n = 50
        for i in range(1, 1 + n):
            label_wgt = QtWidgets.QLabel(f"TextLabel {i}")
            self.scroll_area_content_wgt_lay.addWidget(label_wgt)
        self.scroll_area_content_wgt.setLayout(self.scroll_area_content_wgt_lay)

        # Create a Scroll Area widget
        self.main_wgt_scroll_area = QtWidgets.QScrollArea()

        # You can configure Scroll Area behavior with the following methods
        # self.main_wgt_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.main_wgt_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.main_wgt_scroll_area.setWidgetResizable(True)

        # Set the scroll area content widget as the scroll area only contains one widget, which is the "label_list_wgt"
        self.main_wgt_scroll_area.setWidget(self.scroll_area_content_wgt)

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
    import sys

    app = QtWidgets.QApplication(sys.argv)
    screen_width, screen_height = app.screens()[0].size().toTuple()
    main = MainWindow()
    sys.exit(app.exec())
