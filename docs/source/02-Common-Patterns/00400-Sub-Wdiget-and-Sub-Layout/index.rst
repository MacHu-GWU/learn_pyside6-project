Sub Widget and Sub Layout
==============================================================================
在一个大型 Widget 中, 里面可能包含很多小的 Widget, 这些小的 Widget 都有各自的 Layout. 把逻辑类似的小的 Widget 放在一可复用的类中是一种很好的组织代码的方式. 但是这里有几个很细的问题, 但是会使得最终呈现的效果差别巨大. 这里我们直接把结论放在这里, 如果你已经了解这其中的细节了, 你可以直接参考这里的结论. 而如果你不了解细节, 则建议运行示例代码来查看两者的区别:

1. 把很多 Widget 组织到一起的时候, 是开一个随便什么 Class, 还是一定要开一个 ``PySide6.QtWidgets.QWidget`` 的子类呢?
2. 你可以用一个 Widget 实例来组织多个子 Widget, 把他们都变成自己的属性既可. 但这个父 Widget 本身有一个 ``setLayout`` 的方法. 这里有两种做法:
    1. 在父 Widget 中调用 ``setLayout`` 方法, 然后在 Root Widget 中的 Layout 中, 使用 ``addWidget(父Widget)`` 将父 Widget 添加进来.
    2. 在父 Widget 仅仅是把 Layout 作为一个属性设置好, 但是不调用 ``setLayout``. 然后在 Root Widget 中的 Layout 中, 使用 ``addLayout(父Widget.main_layout)`` 将父 Widget 的 Layout 添加进来.

结论: 这两个问题其实是一个问题. 如果你希望让这些被组织到一起的 Widget 限制在一个隐形的方框容器中, 那么就用 ``PySide6.QtWidgets.QWidget`` + ``root_widget.addWidget()`` 的方式. 这样会将父 Widget 作为一个有边界的整体, 从 Root Widget 是无法直接触碰到 父 Widget 里面的小 Widget 的. 而如果你只是想增加代码复用, 那么你用随便什么 Class 都可以, 仅仅是作为一个内存中的数据容器. 然后用 ``root_widget.addLayout()`` 的方式将父 Widget 的 Layout 添加进来.

.. dropdown:: sub_widget_and_sub_layout_1_1.py

    .. literalinclude:: ./sub_widget_and_sub_layout_1_1.py
       :language: python
       :linenos:

.. dropdown:: sub_widget_and_sub_layout_1_2.py

    .. literalinclude:: ./sub_widget_and_sub_layout_1_2.py
       :language: python
       :linenos:
