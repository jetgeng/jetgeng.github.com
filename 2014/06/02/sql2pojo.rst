在Grails使用Sql获取数据
================================

前因
----

Grails默认情况使用Hibernate作为数据存取的框架。不过Hibernate的缺点是众所周知的。所以我们在一些复杂的场合需要通过 groovy.sql.Sql 直接使用sql来获取数据。这样就会存在如下的问题：

 #. 如何使用Grails配置的数据库连接?
 #. 如何执行sql，进行数据库相关操作?
 #. 如何将查询的数据转换成Domain Class?

下面就从上面这3个问题来说明如何在grails环境中直接使用sql来对数据库进行操作。

连接数据库
----------

连接数据库相对来说比较简单，通过如下代码就可以完成。

.. code-block:: groovy
    :linenos:

    class DoSomethingServices {
        def dataSource

        def queryDataWithSql(){
            Sql sql = new Sql(dataSource)
            sql.each("select * from sometable"){ it ->
                println it 
            }
        }
    }

代码详细说明：

 * 第3行 注入dataSource， 这个dataSource 就是Grails中在DataSource.groovy中配置的 数据源。 默认的hibernate也是在使用这个数据源。
 * 第5 行 使用通过注入的dataSource对象 创建sql对象。 关于Sql对象的使用可以参考 http://groovy.codehaus.org/api/groovy/sql/Sql.html
 * 第6行 使用each方法执行一个sql语句。然后逐行回调。

连接数据库和查询数据就这么简单。

到这里肯定有人会问，如果需要往sql语句中加入参数怎么办。如何避免 Sql注入。
这个Sql在设计的过程中已经考虑到了。而且使用及其简单。只要使用如下代码即可。

.. code-block:: groovy
    :linenos:

        def queryDataWithSql(){
            Sql sql = new Sql(dataSource)
            def paramValue = ..
            def paramValue2 = ..
            sql.each("select * from sometable where field = ${paramValue} and field2 = ${paramValue2}"){ it ->
                println it 
            }
        }

第5行直接使用GString传入参数。最终执行的时候其实是讲GString中得参数获取出来。通过PreparedStatement传入参数的方式。这样可以避免sql的注入的攻击。你不相信？那就看看Sql.java这个类中得eachRow方法吧。这个方法位于groovy-all-2.1.9-source.jar/groovy/sql/Sql.java 的第1236行。

数据如何转换成Domain Class对象
------------------------------------------

这个问题是一个大问题。不过不是没有办法。最笨的办法就是写成如下的样子：

.. code-block:: groovy
    :linenos:

    sql.each("select field1 , field2 from sometable where field = ${paramValue} and field2 = ${paramValue2}"){ it ->
       def someDomain = new SomeDomin()
       someDomain.field1 = it["field1"]
       someDomain.field2 = it["field2"]
    }



   










.. author:: default
.. categories:: none
.. tags:: none
.. comments::
