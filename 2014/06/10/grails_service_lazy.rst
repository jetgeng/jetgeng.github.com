Grails 中服务懒加载
===================

现象
----
前两天在Grails中使用guava的EventBus做消息分发时发现我得一个Subscrib死活没有被调用。很时费解！

我代码的结构如下:

.. code-block:: groovy

    class HandlerAServices {
    
        def eventBus

        @PostConstruct 
        def init(){
            eventBus.register(this)
        }

        @Subscribe
        def someEventHandler(SomeEvent event){
        }
    }

    class HandlerBServices {
        
        def eventBus

        @PostConstruct 
        def init(){
            eventBus.register(this)
        }

        @Subscribe
        def someEventHandler(SomeEvent event){
        }
    }


最后当有SomeEvent这个的事件发出时 发现HandlerBServices 中得someEventHandler 方法被调用，HandlerAServices 中的someEventHandler完全没有执行。 同样的代码，同样的配置啊。怎么会这么邪乎呢！

排查原因
----------


因为grails中对service的初始化在默认情况下采用懒加载的方式。加入一个服务没有被其他的内容如controller，service， domain class等等引用。那么这个服务将不会在已启动的时候就被初始化。
我们的HandlerAServices 中 someEventHandler 没有被执行的原因就是这个HandlerAServices 没有被其他内容直接使用，导致这个HandlerAServices这个bean没有被创建。所以他就没有被调用了。

为了解决这个问题要做的东西很少，只是告诉grails，我们不要懒加载的方式。修改代码如下：

.. code-block:: java

    class HandlerAServices {
        
        static lazyInit = false //申明不需要懒加载
    }

参考资料
--------

# http://grails.1312388.n4.nabble.com/Is-it-possible-to-avoid-lazy-services-initialization-td4646285.html
# http://stackoverflow.com/questions/14832002/postconstruct-fails-silently-on-a-grails-service














.. author:: default
.. categories:: none
.. tags:: none
.. comments::
