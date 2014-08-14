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

求解
----












.. author:: default
.. categories:: none
.. tags:: none
.. comments::
