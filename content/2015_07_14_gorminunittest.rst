对Gorm进行单元测试
#####################


:date: 2015-7-14 17:39
:tags: Gorm; Grails
:category: Grails
:slug: gorminunittest
:summary:
:status: draft


单元测试
----------

在Grails 2.4 以后的版本中，我们就可以对Domain Class进行单元测试了。

起步
------------


.. code-block: groovy

   import grails.test.mixin.TestMixin
   import grails.test.mixin.gorm.Domain
   import grails.test.mixin.hibernate.HibernateTestMixin
   import spock.lang.Specification

   @Domain(Person)
   @TestMixin(HibernateTestMixin)
   class PersonSpec extends Specification {

       void "Test count people"() {
            expect: "Test execute Hibernate count query"
                Person.count() == 0
                sessionFactory != null
                transactionManager != null
                session != null
            }
    }


遇到的问题
---------------


1. hibernate没有找到 引用类。 具体错误如下

.. code-block: bash

   nested exception is org.hibernate.MappingException: Association references unmapped class


2. 没有找到类

.. code-block: bash


   java.lang.ClassNotFoundException: grails.orm.bootstrap.HibernateDatastoreSpringInitializer
