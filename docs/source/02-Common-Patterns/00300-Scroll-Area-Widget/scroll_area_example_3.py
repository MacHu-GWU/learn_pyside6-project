# -*- coding: utf-8 -*-

"""
这个例子演示了如何把 ScrollArea 和其他的 Widget 结合起来放在一起. 使得不是整个窗口
都是滚动区域, 而是只有一部分是滚动区域.

在这个例子中, 我们在 QScrollArea Widget 的上面和下面分别放了很多 QLabel Widget,
并且设定只有 QScrollArea 能够滚动.

这个例子沿用了上一个例子中的代码设计.
"""

from PySide6 import QtWidgets


class ScrollAreaContentWidget(QtWidgets.QWidget):
    """
    由于你必须为 Scroll Area 额外创建一个 Widget 作为容器, 并且 Scroll Area 的 Layout
    其实是在这个容器中完成的, 所以我们单独为 Scroll Area 创建了一个类.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.main_lay = QtWidgets.QVBoxLayout()
        n = 50
        for i in range(1, 1 + n):
            label_wgt = QtWidgets.QLabel(f"TextLabel {i}")
            self.main_lay.addWidget(label_wgt)
        self.setLayout(self.main_lay)


class MainWidget(QtWidgets.QWidget):
    """
    这是 App 主窗口中所有的 Widget 的容器.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.main_lay = QtWidgets.QVBoxLayout()

        # before scroll area
        for i in range(1, 1 + 10):
            label_wgt = QtWidgets.QLabel(f"Before Text Label {i}")
            self.main_lay.addWidget(label_wgt)

        # Create a widget as a container for all other widgets in the scroll area
        self.scroll_area_wgt = QtWidgets.QScrollArea()
        self.scroll_area_content_wgt = ScrollAreaContentWidget(self)
        self.scroll_area_wgt.setWidget(self.scroll_area_content_wgt)
        self.main_lay.addWidget(self.scroll_area_wgt)

        # after scroll area
        for i in range(1, 1 + 10):
            label_wgt = QtWidgets.QLabel(f"After Text Label {i}")
            self.main_lay.addWidget(label_wgt)

        self.setLayout(self.main_lay)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_widget()
        self.set_window()

    def set_widget(self):
        self.main_wgt = MainWidget(self)

    def set_window(self):
        self.setCentralWidget(self.main_wgt)

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
