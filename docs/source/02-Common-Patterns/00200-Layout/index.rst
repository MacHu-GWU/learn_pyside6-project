Layout
==============================================================================


Overview
------------------------------------------------------------------------------
在 GUI 编程中, 一个很重要的概念就是 Layout, 也就是布局. 通过将 Widget 和 Layout 解耦和, 使得我们在编程时能一次只专注于一件事, 并且让整个代码的复用更加灵活. 展开来说就是你可以先专注于定义每个控件细节, 然后最后定义所有 Widget 之间的布局, 也就是 Layout. 如果你改变主意了, 你可以只改动你的 Layout 而不需要改变 Widget.


Examples
------------------------------------------------------------------------------
.. dropdown:: QGridLayout_example.py

    .. image:: ./QGridLayout.png

    .. literalinclude:: ./QGridLayout_example.py
       :language: python
       :linenos:

.. dropdown:: QFormLayout_example.py

    .. image:: ./QFormLayout.png

    .. literalinclude:: ./QFormLayout_example.py
       :language: python
       :linenos:



Reference
------------------------------------------------------------------------------
- `Layout Management <https://doc.qt.io/qtforpython-6/overviews/layout.html>`_: Pyside6 中官方对于 Layout 的介绍.
- `Layout Classes <https://doc.qt.io/qtforpython-6/overviews/layout.html#qt-s-layout-classes>`_: 列出了常用的 Layout 类的详细介绍.
