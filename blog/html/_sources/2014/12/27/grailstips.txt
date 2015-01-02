Grails 技巧汇集
==================

Service 相关
--------------------




读取配置信息
------------

在Config.groovy文件中

.. code-block:: groovy

   my.property = 'some value'


读取配置的任何地方:

.. code-block:: groovy

   def grailsApplication

   grailsApplication.config.my.property 







.. author:: default
.. categories:: none
.. tags:: Grails
.. comments::
