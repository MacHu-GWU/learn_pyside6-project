Scroll Area Widget
==============================================================================
在竖着排列所有 Widget 的过程中, 很可能一个窗口是无法放下所有的 Widget 的, 这时就要用到 ``QScrollArea`` 这个 Widget.

使用这个 ``scroll_area_widget = QScrollArea(...)`` 的关键是你需要把所有想要放在这个 Scroll Area 中的 Widget 专门放在一个单独的 ``scroll_area_content_widget = QWidget(...)`` 容器中. 你用 ``scroll_area_content_widget.setLayout(...)`` 方法对这个 Widget 进行布局. 然后用 ``scroll_area_widget.setWidget(scroll_area_content_widget)`` 方法把这个 ``scroll_area_content_widget`` 放到 ``scroll_area_widget`` 中.

.. dropdown:: scroll_area_example_1.py

    .. literalinclude:: ./scroll_area_example_1.py
       :language: python
       :linenos:

.. dropdown:: scroll_area_example_2.py

    .. literalinclude:: ./scroll_area_example_2.py
       :language: python
       :linenos:

.. dropdown:: scroll_area_example_3.py

    .. image:: ./nested-scroll-area.png

    .. literalinclude:: ./scroll_area_example_3.py
       :language: python
       :linenos:

