QLineEdit Widget
==============================================================================
keywords: QLineEdit, LineEdit, Line Edit

Line Edit Widget 是最简单的用于跟用户交互的输入控件. 它允许用户输入单行文本.

它有这么几个 Signal:

- cursorPositionChanged: 当光标位置改变时触发.
- editingFinished: 当这个控件失去焦点时 (你点击了另一个 widget) 触发. 这样可以避免在编辑的过程中 ``textChanged``, ``textEdited`` 频繁触发.
- inputRejected: 如果你给 line edit 通过 setValidator 方法设置了 validator, 当用户输入不合法时触发.
- returnPressed: 当用户按下回车时触发.
- selectionChanged: 当用户用鼠标选定了一段文本, 并且选定的文本发生变化时触发.
- textChanged: 只要文本发生变化, 就会触发.
- textEdited: 跟 textChanged 不同, 只有用户在编辑时输入了信文本, 才会触发. 而你如果用 setText API 改变了这个文本, 则不会触发.


Examples
------------------------------------------------------------------------------
.. dropdown:: line_edit_widget_1.py

    .. literalinclude:: ./line_edit_widget_1.py
       :language: python
       :linenos:


Reference
------------------------------------------------------------------------------
- `QLineEdit <https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLineEdit.html>`_
