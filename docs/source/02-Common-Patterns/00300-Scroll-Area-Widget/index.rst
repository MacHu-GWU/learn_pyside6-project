Scroll Area Widget
==============================================================================
这是一个用于演示如何使用 ``QScrollArea`` 来创建一个可以滚动的区域.

有的时候一个窗口是无法放下所有的 Widget 的, 这时就要用到 ``QScrollArea`` 这个 Widget. ``QScrollArea`` 本质上是一个大小有限制的矩形区域, 里面的元素如果超过了这个区域则会自动出现滚动条. ``QScrollArea`` 在 GUI 中非常有用. 它不仅能滚动整个 App 的窗口, 也可以把作为一个小的滚动区域跟其他的 Widget 放在一起.

.. dropdown:: scroll_area_example_1.py

    .. literalinclude:: ./scroll_area_example_1.py
       :language: python
       :linenos:

.. dropdown:: scroll_area_example_2.py

    .. literalinclude:: ./scroll_area_example_2.py
       :language: python
       :linenos:

.. dropdown:: scroll_area_example_3.py

    .. literalinclude:: ./scroll_area_example_2.py
       :language: python
       :linenos:

.. dropdown:: scroll_area_example_4.py

    .. image:: ./nested-scroll-area.png

    .. literalinclude:: ./scroll_area_example_3.py
       :language: python
       :linenos:

