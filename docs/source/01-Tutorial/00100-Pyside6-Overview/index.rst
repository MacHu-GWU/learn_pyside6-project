Pyside6 Overview
==============================================================================


1. What is QT
------------------------------------------------------------------------------
在介绍 PySide6 之前, 必须要了解一下 `QT <https://www.qt.io/>`_. QT 是一个历史和 Python 一样悠久的 GUI (桌面 App) 的 C++ 框架, 都是 90 年代初的产物, 也是目前最流行的 GUI 框架之一, 文档和教程也非常多, 是一个非常成熟的框架. 本项目是我在学习 QT 从入门到精通 (现在还谈不上精通) 的过程中的文档. 致力于让我自己能快速的回顾和查找, 也希望能帮助到其他人.


2. What is QT for Python? How about PySide and PyQT?
------------------------------------------------------------------------------
QT 是一个 C++ 框架, 原本并不支持 Python, 但是由于有经验的 C++ 开发者太难得了, 而 Python 又是如此的简单易学, 所以一个商业公司 Riverbank Computing (RC) 就开发了 PyQT, 并于 1998 年发布. 但是它的开源协议是 GPLv3. 也是如果你不缴费购买商业协议, 那么你用 PyQT 开发的软件也必须开源. 而如果你要开发商用闭源软件就要购买它的商业协议 (约 $550/年). 当时 QT 的母公司 Nokia 找到 RC, 希望能让它支持对商业用户更友好的 LGPL 协议, 当然 RC 为了商业利润是不干的. 而 Nokia 就决定单干, 于是在 2009 年发布了 `PySide <https://en.wikipedia.org/wiki/PySide>`_, 并采用了 LGPL 协议. 简单来说就是允许你用它开发商业程序而无需付费.

到目前 (2023 年 5 月) 为止, QT 的版本是 6.X, 而 PySide6 自 2020 年 12 月发布以来, 文档和资料页比较丰富了, 所以我选择了 PySide6 作为我的主力 GUI 开发工具. 在这之后我但凡提到 QT 或是 PySide6, 都是指的同一个东西.

Reference:

- `QT History <https://wiki.qt.io/Qt_History>`_


3. How do I Start Learning?
------------------------------------------------------------------------------
我们了解了背景之后, 要如何开始学习呢? 下面两个链接是我学习 QT 的主要参考资料, 其中 FAQ 的这篇文档建议在第一次接触 QT 的时候完整的通读一遍, 里面介绍了 QT, QML, Widgets, Python 和 C++ binding 等重要概念, 如果不理解这些概念是无法学下去的:

- `QT for Python 官方文档 <https://doc.qt.io/qtforpython-6/quickstart.html>`_
- `QT for Python FAQ <https://doc.qt.io/qtforpython-6/quickstart.html#faq-section>`_


4. How could I create my First GUI App?
------------------------------------------------------------------------------
你可能迫不及待的想要开始做一个 GUI App 了. `QT Tutorials <https://doc.qt.io/qtforpython-6/tutorials/index.html>`_ 是一个非常赞的教学文档. 它通过一些简单的例子来帮助开发者理解 QT 的编程模型, 核心概念, 以及各种设计模式. 作为一个入门教程, 里面的例子都非常简单. 建议至少上手把代码拷到 IDE 里跑一边, 至少要掌握如下概念:

- Widget.
- Signal and Slot (非常重要, GUI 软件用的是事件驱动编程模型, 这是 QT 里实现用户交互的核心机制).
- ``.ui``, ``.qml``, ``.qrc`` 文件.

然后建议精读 `Expenses Tool Tutorial <https://doc.qt.io/qtforpython-6/tutorials/expenses/expenses.html>`_ 这个钱包支出管理 App 的例子, 里面包含了一个最常见的 App 所需要的核心组件.


5. How could I create my first Production ready App?
------------------------------------------------------------------------------
你已经掌握了 QT 的基本知识了, 现在你可能想开始做一个真正 "有用" 的 App 了. 我建议直接动手开始做, 遇到自己想要实现的模式但是 Tutorial 里面没教的时候, 查找 `QT Examples <https://doc.qt.io/qtforpython-6/examples/index.html>`_ 这篇文档, 里面包含了 184 个从简单到非常复杂的 App 例子, 基本包含 QT 所有的技巧和知识点. 但我不建议直接就开始学 Examples, 而是在自己做 App 的时候有需要再去查找, 循序渐进.

到最后当你开发完成了一个 "有用" 的 App 之后, 你需要学习如何将它打包分发给别人用. 这个过程叫做 "Deployment". `QT Deployment <https://doc.qt.io/qtforpython-6/deployment/index.html>`_ 是一篇详细的说如何打包分发的文档. 我建议你用一个简单的 Hello World App 来学习 Deployment, 而不是用你构建好的那个复杂的 "有用" 的 App. 当你理解了 Deployment 的机制之后, 再尝试用它来打包你的 "有用" 的 App.


6. Summary
------------------------------------------------------------------------------
以上就是我从入门到精通所经历的过程, 其中我在 #4 这一步创建了十多个大大小小的 App, 才逐渐能熟练的开发桌面 GUI. 祝你学习愉快.
