让Netty接受WebSocket请求 
==============================

缘起
------------------------------------------------------------    

最近有个需要要求让 `JBoss AS 7`_ 支持WebSocket请求。遇到这样的问题，我的第一反应就是去想办法去换掉 `Jboss AS 7`_ 中的tomcat 容器或者把HTTP请求转发到另外一个容器中。一个老外 `JBoss 7 and WebSocket`_ 中就这么干的。但是觉得还存在一些问题。
所以一直在尝试其他方案，突然一天看到了Netty的架构图。发现他居然支持WebSocket接入。如果我做一个subsystem，把Netty装进去是不是就可以解决这个问题呢？

尝试
------------------------------------------------------------    

有这如上的想法以后，就得去验证。验证的第一步就是确定Netty是否真的能够支持WebSocket。什么话都不用说了上让代码证明一切吧！


.. uml::

    interface AttributeMap{
    }
    interface ChannelOutboundInvoker{
        bind()
        connect()
        disconnect()
        close()
        deregister()
        flush()
        write(message:Object)
    }
    interface ChannelFutureFactory{
    }
    interface Channel{
        isOpen()
        isRegistered()
        isActive()
        
    }

    AttributeMap <|-- Channel
    ChannelOutboundInvoker <|-- Channel
    ChannelFutureFactory <|-- Channel 

    DefaultChannelGroup
    note of DefaultChannelGroup : 可以保存多个Channel。 



.. _JBoss 7 and WebSocket: http://golovnin.blogspot.com/2012/04/jboss-7-and-websockets.html
.. _JBoss AS 7: http://www.jboss.org/as7

.. author:: default
.. categories:: Jboss 
.. tags:: Netty 
.. comments::
