# -*- coding: utf-8 -*-

"""
这个例子跟上一个例子的效果一摸一样, 不过我们对代码进行了一些设计, 使得代码更加清晰.
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


class MainWidgetScrollArea(QtWidgets.QScrollArea):
    """
    由于我们的 App 窗口中有且只有一个 QScrollArea, 所以这个 MainWidget 就是 QScrollArea.
    的子类.
    """

    def __init__(self, parent):
        super().__init__(parent)
        # Create a widget as a container for all other widgets in the scroll area
        self.scroll_area_content_wgt = ScrollAreaContentWidget(self)
        # Set the scroll area content widget as the scroll area only contains one widget, which is the "label_list_wgt"
        self.setWidget(self.scroll_area_content_wgt)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_widget()
        self.set_window()

    def set_widget(self):
        self.main_wgt_scroll_area = MainWidgetScrollArea(self)

    def set_window(self):
        # set the "main_wgt_scroll_area" as central widget in App window
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
