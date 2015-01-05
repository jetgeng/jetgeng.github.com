Grails 技巧汇集
==================

Service 相关
--------------------


配置相关
--------



获取当前环境
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: java

    import import grails.util.Environment
    def currentEnvName = Environment.current
    // currentEnvName 有可能是： "production" 线上环境
    //                            'beta'    beta环境
    //                            'dev'






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
