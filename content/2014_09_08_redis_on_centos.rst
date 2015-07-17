在CentOS上安装Redis
==============================


:date: 2014-9-14 17:39
:tags: Gorm; Grails
:category: 系统维护

redis 用的人越来越到。他在linux上安装也很简单。官方文档http://redis.io/topics/quickstart 已经说的很清楚了。

不过在CentOS 上遇到了问题。我的CentOS是一个很干净的系统，没有装过任何其他的东西。所以编译用的gcc 都没有。在Debian 系统中一句 ``` apt-get  build-essential ``` 就可以搞定一切了。
在CentOs中是不是有对应的呢，当然是有了！

.. code-block:: bash

   sudo yum groupinstall "Development Tools"


这样就搞定了！ 可以继续使用make命令来执行了。

不过要命的是我用的是CentOS release 6.5 (Final) 遇到了他的那个 #error "Newer version of jemalloc required" 错误。这个是让我升级jemalloc的节奏啊。

我去那里找这个jemalloc啊？不要找其实已经有了。

.. code-block:: bash

   cd deps
   make hiredis jemalloc linenoise lua
   cd ..
   make install

这个事情就这么搞定了！


这个解决方案源自 http://unix.stackexchange.com/questions/94479/jemalloc-and-other-errors-making-redis-on-centos-6-4
