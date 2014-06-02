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

这个方法最大的缺点是代码量多，并且会有大量重复的代码。给人感觉很恶心。
在Groovy中又如下的办法可以对对象的字段赋值：

.. code-block:: groovy
    :linenos:

     def key = "field1"
     someDomain.getProperties()[key] = "someValue"

getProperties这个方法将该对象的所有值放到一个Map中返回。具体可参考http://groovy.codehaus.org/groovy-jdk/java/lang/Object.html#getProperties%28%29 对这个map进行赋值，就等于对这个对象进行赋值。
所以下面我只要有一个字段和变量名对应的map，什么就会搞定了。
于是有了如下的代码：

.. code-block:: groovy
    :linenos:

    class DomainClassInfoService {
    
        def sessionFactory
        def grailsApplication
    
        def getDomainClass(clazzName) {
            return grailsApplication.domainClasses.find {
                it.name == clazzName
            }
        }
    
        def getFieldColumnMap(clazz) {
            def fieldColumnMap = [:]
            def hibernateMetaClass = sessionFactory.getClassMetadata(clazz)
            def grailsDomainClass = getDomainClass(clazz.getSimpleName())
            def domainProps = grailsDomainClass.getProperties()
    
            domainProps.each { prop ->
                //get the property's name
                def propName = prop.getName()
                //please refer to the hibernate javadoc
                //http://www.hibernate.org/hib_docs/v3/api/org/hibernate/persister/entity/AbstractEntityPersister.html
                def columnProps = hibernateMetaClass.getPropertyColumnNames(propName)
                if (columnProps && columnProps.length > 0) {
                    //get the columnname, which is stored into the first array
                    def columnName = columnProps[0]
                    fieldColumnMap[propName] = columnName
                }
            }
            return fieldColumnMap
        }
    }

以上代码说明如下：
 * 5 ~ 6 行注入将要使用的两个服务，一个是hibernate的sessionFactory， 另外一个是grailsApplication 上下文
 * 7 ~ 9 这个方法是根据给定的段类名。比如有一个Domain Class的全名为 org.gunn.domain.Book 这里的clazzName 就是Book。
   * 第 8 行是从grailsApplication中获取所有Domain Class的DefaultGrailsDomainClass这个类的对象。这里牵涉到一个Artefact的概念，请参考 https://grails.org/Developer+-+Artefact+API
 * 12 ~ 28 行就是 根据Domain Class中的变量来获取数据库对应的的字段名。 有代码在这里就不多解释了。

结合我们上面的那个properties的小技巧，我们就使用如下代码来完成使用Sql查询数据，转换成Domain Class的对象。

.. code-block:: groovy
    :linenos:

    String querySql = ''' select * from table where field1 = ? '''

    def tripSegmentFieldColumnMap = domainClassInfoService.getFieldColumnMap(SomeDomain)
    Sql sql = new Sql(dataSource)
    sql.eachRow(querySql, field1Value){
       SomeDomain someObject = new SomeDomain() 
       tripSegmentFieldColumnMap.each { key, value ->
            someObject.getProperties()[key] = it[value]
       }
     }

这个方法对于非关系的，没有太大问题。如果有类似于一对多这样的关系的话，会引起hibernate中著名的n+1的问题。例如SomeDomain 中有一个变量是SomeParent, 并且SomeDomain belong to 这个SomeParent的话。那么像上面那样直接赋值就会引起去发起数据库查询请求查询SomeParent的。所以可以使用如下的方式进行避免：

.. code-block:: groovy

    
    sql.eachRow(querySql, field1Value){
       SomeDomain someObject = new SomeDomain() 
       SomeParent someParent = new SomeParent()
       someParent.id = it.parentId
       tripSegmentFieldColumnMap.each { key, value ->
            if(key != "parentId")
                someObject.getProperties()[key] = it[value]
       }
       someObject.parent = someParent

这个办法很土，如果你又更好的。欢迎分享！谢谢！


   





   










.. author:: default
.. categories:: none
.. tags:: none
.. comments::
