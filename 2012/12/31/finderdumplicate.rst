又一个查找重复文件的工具
==========================

有一块放了很多照片的硬盘，想整理出来另作他用。由于当时偷懒，把照片放的乱。甚至有一张照片放了很多份。浪费空间不说，主要是找个东西太费劲。
所以就下决心自己写一个小工具把这些照片整理整理。

技术方案
------------------------------------------------------------    

 1. 这种小东西用Python写会很快。就不用多想了。直接用他就OK了。
 #. `argparse <http://pypi.python.org/pypi/argparse>`_ , 用来做命令的解析。
 #. `sh <http://pypi.python.org/pypi/sh/1.07>`_ ,用于执行一些命令。
 #. 使用git hash-object 命令获取文件的sha1
 
设计思路
------------------------------------------------------------    

这是一个命令行软件。命令行格式为：

.. code-block:: bash

    ./fileDupFinder.py -e Extend -s sourcefolder -t targetfolder


参数选项    长选项  用途
-e          --extend    将要处理文件的扩展名，不区分大小写
-s          --source    处理的源目录
-t          --target    处理的输出目录
.. uml::

    class {
    }


.. author::Jet Geng 
.. categories::Python 
.. tags:: Python
.. comments::
