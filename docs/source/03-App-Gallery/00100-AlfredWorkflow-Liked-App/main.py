# -*- coding: utf-8 -*-

# 任何面向最终用户的 app 基本上都是从命令行接入的, 所以 sys 模块是必须的
import sys

# QtCore, QtWidgets, QtGui 是 PySide 的三个主要模块, 一般每一个项目都会用到这三个模块.
# 所以我一般在开始就会 Import 它们, 不管用不用得到.
# 全部的模块列表: https://doc.qt.io/qtforpython-6/modules.html#
from PySide6 import QtCore, QtWidgets, QtGui
import json
from pathlib import Path


class MainWindow(QtWidgets.QMainWindow):
    """
    一般任何一个 App 都有一个主窗口. 在这个主窗口里我们可以塞下各种各样的 Widget.
    """

    def __init__(self, widget: QtWidgets.QWidget):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("Alfred Liked App")
        self.add_menu()
        self.setCentralWidget(widget)

    def add_menu(self):
        # Create the tray
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setIcon(QtGui.QIcon("icon.png"))
        self.tray.setVisible(True)

        # Create the menu
        self.menu = QtWidgets.QMenu()
        self.file_menu = self.menu.addMenu("File")

        settings_action = QtGui.QAction("settings", self)
        settings_action.triggered.connect(self.update_settings)

        self.file_menu.addAction(settings_action)
        self.tray.setContextMenu(self.menu)

    @QtCore.Slot()
    def update_settings(self, checked):
        print("update settings")


class TabDialog(QtWidgets.QDialog):
    """
    这是我们主要的 Widget, 它包含了多个 Tab.

    每个 Tab 本身是一个子 Widget.
    """

    def __init__(self, parent: QtWidgets.QWidget = None):
        super().__init__(parent)
        self.tab_widget = QtWidgets.QTabWidget()

        # 一共有两个 Tab, 一个用于搜索, 一个用于设置
        self.tab_widget.addTab(SearchWidget(self), "Search")
        self.tab_widget.addTab(SettingsWidget(self), "Settings")

        # 这个 Widget 只有一个 Layout, 用于放置 Tab
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)


class SearchWidget(QtWidgets.QWidget):
    """
    Alfred 的 Search Input box Widget, 包含了一个输入框和一个下拉框.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)

        self.add_dropdown_items()
        self.add_input_box()
        self.set_layout()

    def add_dropdown_items(self):
        # 创建一个 ListWidget 作为 dropdown items 的容器
        self.item_list = QtWidgets.QListWidget()
        # 将 item list 设置为单选模式, 它一共有以下几种模式可供选择
        #
        # - NoSelection
        # - SingleSelection
        # - MultiSelection
        # - ExtendedSelection
        # - ContiguousSelection
        self.item_list.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        # 当用户双击某个 item 的时候, 会触发 itemDoubleClicked 事件
        # 我们将其与一个函数绑定, 用来处理这个事件
        self.item_list.itemDoubleClicked.connect(
            self.item_list_item_double_clicked_event_handler
        )
        self.set_n_items(3)

    def set_n_items(self, n: int):
        self.item_list.clear()
        for i in range(1, 1 + n):
            item = QtWidgets.QListWidgetItem(f"Item {i}")
            item.setTextAlignment(QtCore.Qt.AlignLeft)
            self.item_list.addItem(item)

    def item_list_item_double_clicked_event_handler(self):
        """
        当用户双击 dropdown items 中的某个 item 的时候会触发这个函数. 也就是 Alfred 中
        的 action. 在 Alfred 中你可以点击, 也可以用 Enter, Ctrl + C 等各种快捷键.
        在这个极简的例子中我们就用双击来代表 Alfred 中的点击
        """
        text = self.item_list.selectedItems()[0].text()
        print(f"item list item double clicked: {text!r}")
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(text)

    def add_input_box(self):
        # 创建一个 LineEdit 作为输入的文本框
        self.input_box = QtWidgets.QLineEdit()
        self.input_box.setPlaceholderText("enter a 1 - 10 number here")
        self.input_box.textChanged.connect(self.input_box_text_changed_event_handler)

    def input_box_text_changed_event_handler(self):
        """
        当输入框的内容发生变化时, 会触发这个函数. 这个相当于 Alfred Workflow 里面的
        Script Filter.
        """
        text = self.input_box.text()
        print(f"input box text changed to {text!r}")
        try:
            n = int(text)
            if n > 10:
                n = 10
            elif n < 0:
                n = 0
            else:
                pass
        except Exception:
            n = 3
        self.set_n_items(n)

    def set_layout(self):
        # QVBoxLayout is a vertical layout, which means it will stack widgets vertically.
        # there's another layout called QHBoxLayout (horizontal layout).
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.input_box)
        layout.addWidget(self.item_list)
        self.setLayout(layout)


path_settings = Path(__file__).absolute().parent.joinpath("settings.json")


def read_settings() -> dict:
    try:
        return json.loads(path_settings.read_text())
    except FileNotFoundError:
        path_settings.write_text(json.dumps("{}"))
        return {}


def write_settings(data: dict):
    path_settings.write_text(json.dumps(data, indent=4))


class SettingsWidget(QtWidgets.QWidget):
    """
    用于设置的 Widget, 包含了许多 Key Value 的输入框.
    """

    def __init__(self, parent: QtWidgets.QWidget):
        super().__init__(parent)
        self.setting_keys = ["key1", "key2"] # 定义我们的 config 有哪些 Key
        self.add_settings_form()
        self.add_buttons()
        self.set_layout()

    def add_settings_form(self):
        # 创建一个用于展示 settings 中的 key value 的表格
        self.setting_form: dict[str, tuple[QtWidgets.QLabel, QtWidgets.QLineEdit]] = {}
        data = read_settings()
        # 从列表动态生成 key value 的表单
        for key in self.setting_keys:
            # 其中 key 是一个 label
            label = QtWidgets.QLabel(f"{key}:")
            # 而 value 是一个输入框
            edit = QtWidgets.QLineEdit()
            edit.setPlaceholderText("type something here")
            # 默认第一次打开的时候会从 settings 中读取数据
            if key in data:
                edit.setText(str(data.get(key)))
            self.setting_form[key] = (label, edit)

    def add_buttons(self):
        # 添加两个 button, 一个用于从 settings 中加载数据, 另一个用于将数据写入 settings
        self.load_button = QtWidgets.QPushButton("Load")
        self.load_button.clicked.connect(self.load_button_clicked_event_handler)
        self.apply_button = QtWidgets.QPushButton("Apply")
        self.apply_button.clicked.connect(self.apply_button_clicked_event_handler)

    @QtCore.Slot()
    def load_button_clicked_event_handler(self):
        data = read_settings()
        for key, value in self.setting_form.items():
            if key in data:
                value[1].setText(str(data.get(key)))

    @QtCore.Slot()
    def apply_button_clicked_event_handler(self):
        write_settings(
            {key: value[1].text() for key, value in self.setting_form.items()}
        )

    def set_layout(self):
        # 设置一个嵌套的 layout, 其中 form layout 是子 layout
        form_layout = QtWidgets.QVBoxLayout()
        for key, value in self.setting_form.items():
            form_layout.addWidget(value[0])
            form_layout.addWidget(value[1])

        # button 的 layout 也是一个子 layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.apply_button)

        # 最后将两个子 layout 组合起来
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    tab_dialog = TabDialog()

    window = MainWindow(tab_dialog)  # 将主要的 widget 添加到 MainWindow 中
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec())
