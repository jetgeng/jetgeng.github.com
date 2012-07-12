JBoss AS 7 学习笔记
===============

XNIO模块
------------------------------------------------------------    

我们先从jboss-as-remoting-test的着手了解他。
在RemotingSubsystemTestCase中

.. uml::

    class AbstractSubsystemBaseTest{
    }

    class RemotingSubsystemTestCase{
    }

Netty模块
------------------------------------------------------------    

这个东西是和MINA项目对等的。但是他的野心会大一点。直接支持web socket。有点意思。

.. author:: default
.. categories:: JBoss 
.. tags:: JBoss 
.. comments::
