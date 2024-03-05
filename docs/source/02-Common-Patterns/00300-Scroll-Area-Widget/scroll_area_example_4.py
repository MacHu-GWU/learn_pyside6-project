# -*- coding: utf-8 -*-

"""
这个例子演示了如何把 ScrollArea 内签到其他 Scroll Area 中.

在这个例子中, App 的主窗口是一个大的 Scroll Area, 里面包含了两个 Scroll Area Widget.
你既可以单独滚动每一个小的 Scroll Area, 也可以滚动整个大的 Scroll Area.

这个例子沿用了上一个例子中的代码设计.
"""

from PySide6 import QtWidgets


class SubScrollAreaContentWidget(QtWidgets.QWidget):
    """
    这是 sub scroll area 中所有 widget 的容器. 里面包含了很多 label widget.
    """

    def __init__(self, parent, prefix: str):
        super().__init__(parent)
        self.main_lay = QtWidgets.QVBoxLayout()
        n = 50
        for i in range(1, 1 + n):
            label_wgt = QtWidgets.QLabel(f"{prefix} {i}")
            self.main_lay.addWidget(label_wgt)
        self.setLayout(self.main_lay)


class SubScrollAreaWidget(QtWidgets.QScrollArea):
    """
    这是 sub scroll area widget 对象. 里面有且只有一个 widget, 也就是
    :class:`SubScrollAreaContentWidget`
    """

    def __init__(self, parent, prefix: str):
        super().__init__(parent)
        self.scroll_area_content_wgt = SubScrollAreaContentWidget(self, prefix=prefix)
        self.setWidget(self.scroll_area_content_wgt)


class MainScrollAreaContentWidget(QtWidgets.QWidget):
    """
    这是 scroll area 中所有 widget 的容器. 里面包含了很多 2 个 sub scroll area.
    """

    def __init__(
        self,
        parent,
    ):
        super().__init__(parent)
        self.main_lay = QtWidgets.QVBoxLayout()
        self.sub_scroll_area_wgt_1 = SubScrollAreaWidget(
            self,
            prefix="Sub Scroll Area 1 -",
        )
        self.sub_scroll_area_wgt_2 = SubScrollAreaWidget(
            self,
            prefix="Sub Scroll Area 2 -",
        )
        self.main_lay.addWidget(self.sub_scroll_area_wgt_1)
        self.main_lay.addWidget(self.sub_scroll_area_wgt_2)
        self.setLayout(self.main_lay)


class MainWidgetScrollArea(QtWidgets.QScrollArea):
    """
    由于我们的 App 窗口中有且只有一个 QScrollArea (虽然里面包含了两个 sub scroll area),
    所以这个 MainWidget 就是 QScrollArea 的子类.
    """

    def __init__(self, parent):
        super().__init__(parent)
        # Create a widget as a container for all other widgets in the scroll area
        self.scroll_area_content_wgt = MainScrollAreaContentWidget(self)
        # Set the scroll area content widget as the scroll area only contains one widget, which is the "label_list_wgt"
        self.setWidget(self.scroll_area_content_wgt)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.set_widget()
        self.set_window()

    def set_widget(self):
        self.main_wgt = MainWidgetScrollArea(self)

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
