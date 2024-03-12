Widgets Overview
==============================================================================
本文总结了常用 Widgets.


Display Information
------------------------------------------------------------------------------
这里的 widget 通常用于显示信息.

- `QLabel <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html>`_: 显示文本. 常用于显式单行文本. 例如显式 Key Value Pair.
- `QTextBrowser <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTextBrowser.html>`_: 显示多行富文本, 但是不可编辑.
- `QListWidget <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidget.html>`_: 用于显式列表数据. 例如文件浏览器中的文件列表, dropdown 中的数据列表等.
- `QListWidgetItem <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListWidgetItem.html>`_: QListWidget 中的 item 的容器.
- `QListView <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QListView.html>`_: 这是一个抽象的 list 的试图, 他是 QListWidget 的父类. 换言之 QListWidget 是封装号的 QListView, 更容易使用. 而如果你需要对其进行复杂的自定义, 那么建议使用 QListView.
- `QTableWidget <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidget.html>`_: 用于显式二维表数据.
- `QTableWidgetItem <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableWidgetItem.html>`_: QTableWidget 中的 item 的容器.
- `QTableView <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTableView.html>`_: 和 QListView 类似, 它是 QTableWidget 的父类. 如果你要复杂的自定义功能, 那么建议使用 QTableView.
- 关于图像, 视频等内容的显式, 不属于 Widgets 的范畴, 请参考 `QtGui <https://doc.qt.io/qtforpython-6/PySide6/QtGui/index.html>`_ 一节的内容.


User Input
------------------------------------------------------------------------------
这里的 widget 通常用于让用户输入信息. 对于 search as you type 的应用, 你可以让用户输入信息的过程中就不断触发 event, 从而实现实时反馈.

- `QLineEdit <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html>`_: 单行文本输入框.
- `QTextEdit <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTextEdit.html>`_: 多行文本输入框.
- `QSpinBox <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSpinBox.html>`_: 具有上下按钮的数字输入框, 用于输入整数.
- `QDoubleSpinBox <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDoubleSpinBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QDoubleSpinBox>`_: 和 QSpinBox 类似, 不过用于输入小数.
- `QSlider <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QSlider.html>`_: 滑动条, 用于调整非精确的数值.
- `QDial <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDial.html>`_: 旋钮表盘, 用于调整非精确的数值.
- `QDateTimeEdit <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateTimeEdit.html>`_: 日期时间输入框.
- `QDateEdit <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDateEdit.html>`_: 日期输入框.
- `QCompleter <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCompleter.html>`_: 所有的输入 widget 都可以用这个类来设置自动补全.


Button
------------------------------------------------------------------------------
这里的 widget 通常用于按钮. 当用户跟这些按钮交互时往往会触发一些 event.

- `QPushButton <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html>`_: 按钮
- `QCheckBox <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QCheckBox.html#PySide6.QtWidgets.PySide6.QtWidgets.QCheckBox>`_: 勾选框, 常用于 boolean 选项.
- `QRadioButton <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QRadioButton.html#PySide6.QtWidgets.PySide6.QtWidgets.QRadioButton>`_: 单选框, 在多个选项中你只能选择一个.
- `QToolButton <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolButton.html#PySide6.QtWidgets.PySide6.QtWidgets.QToolButton>`_: 工具栏, 类似于 Word 里上面的一条工具栏.
- `QGroupBox <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGroupBox.html>`_: 将多个 widget 放在一个框里, 并将其作为逻辑上的一个 Group. 常用于将 radio 和 checkbox 分组存放.


Container
------------------------------------------------------------------------------
- `QWidget <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget>`_: 所有 widget 的基类, 通常用于自定义 widget 或是作为其他 widget 的容器.
- `QFrame <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFrame.html>`_: 一个外部有一个边框的 widget, 通常用于分割 widget.
- `QScrollArea <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QScrollArea.html>`_: 区域大小有限制, 如果里面的 widget 太多, 会自动出现滚动条.


Layout
------------------------------------------------------------------------------
- `QLayout <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLayout.html>`_: 所有的 layout 的基类.
- `QVBoxLayout <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QVBoxLayout.html>`_: 垂直布局, 将 widget 垂直排列.
- `QHBoxLayout <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QHBoxLayout.html>`_: 水平布局, 将 widget 水平排列.
- `QGridLayout <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QGridLayout.html>`_: 网格布局, 将 widget 按照网格排列.
- `QFormLayout <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFormLayout.html>`_: 表单布局, 将 widget 按照表单排列. 本质上是一个两列的 ``QGridLayout``.
- `QWidgetItem <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidgetItem.html>`_: 虽然它是一个 widget, 在使用起来更像是一个 layout, 专门用于把很多 widget 按照一定的 layout 组织在一起. 以避免复杂的嵌套.


GUI
------------------------------------------------------------------------------
- `QMainWindow <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMainWindow.html>`_: 一个 GUI 通常要有一个主要的窗口.
- `QMenu <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenu.html>`_: 用于实现操作系统上的菜单 (通常位于顶部).
- `QMenuBar <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QMenuBar.html>`_: 用于实现操作系统上的一条菜单栏 (通常位于顶部).
- `QDockWidget <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDockWidget.html>`_: 一个可以悬停在窗口上的 widget.


Dialog
------------------------------------------------------------------------------
所谓 `dialog <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialog.html#more>`_ 就是一个主要用于跟用户交互的 widget. 例如弹出一个选择文件的窗口, 弹出一个要你输入数字或者文本的窗口. 它的生命周期较短. 这里有个 "模态" 的概念. 所谓 "模态" 就是指当你进入 dialog 后, 会阻止你跟 GUI 的其他部分, 通常是 main window 交互. 当然 dialog 既可以是模态的, 也可以是非模态的. 只不过大部分的 dialog 都被设计为模态的.

- `QDialog <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QDialog.html>`_
- `QFileDialog <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QFileDialog.html>`_
- `QInputDialog <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QInputDialog.html>`_
- `QProgressDialog <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QProgressDialog.html>`_


Tab
------------------------------------------------------------------------------
- `QTabWidget <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabWidget.html>`_: 一个标签页. 每个标签页都可以放一个 widget.
- `QTabBar <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QTabBar.html>`_: 用于实现标签页的标签栏.


Wizard
------------------------------------------------------------------------------
- `QWizard <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWizard.html>`_: wizard 是用于指导用户完成一系列操作的的特殊窗口类型小部件.
- `QWizardPage <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWizardPage.html>`_: 用于实现 wizard 的页面. 本质上是一个容器.



Other
------------------------------------------------------------------------------
- `QToolTip <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QToolTip.html>`_: 一个小的提示框, 用于显示提示信息.
- `QWhatsThis <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWhatsThis.html>`_: 鼠标悬停在 widget 上时显示帮助信息. 通常不会直接使用, 而是通过 `setWhatsThis <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.setWhatsThis>`_ 方法设置 (所有的 widget 都有这个方法).
