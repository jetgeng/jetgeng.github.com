Grails开发手记 -- 准备环境 
========================================

我使用的环境是Linux和Mac，所以我使用的工具主要是Linux下的。在windows下面可以通过  `Cygwin <www.cygwin.com>` 获取本文所说的工具。

工具列表
--------

 `gvm <http://gvmtool.net/>`
    帮助你方便的管理各个版本的groovy，grails等内容。感觉很贴心！推荐
 `Grails Bash Completion <http://www.grails.org/Grails%20Bash%20Completion>` 
    在做grails开发的时候经常用到命令行，比如grails run-app, grails generate-domain-class 之类的命令。老是不停的重复敲挺烦人的。所以有好人做这个工具。直接在命令行中tab，居然能带出domain class 的包名。非常cool！

开始安装
--------

打开命令行：

.. code-block:: bash

   curl -s get.gvmtool.net | bash

   gvm install grails



注意的问题
----------

Service 中的类名必须要要和文件名一致。



.. author:: Jet Geng 
.. categories:: Grails
.. tags:: none
.. comments::
