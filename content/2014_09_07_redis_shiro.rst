使用Redis让Shiro实现集群
============================================


:date: 2014-09-07 17:39
:tags: Gorm; Grails
:category: Grails

在使用shiro是一个很不错的权限验证框架。我们要在一个多机同时活的结构中使用他来做权限管理。这里就牵涉到一个认证Session共享的问题。我们决定使用redis作为这个Session存储的介质。
所以在github上发现了https://github.com/alexxiyang/shiro-redis 这个项目。这个项目基本上解决了我的问题。
不过在使用的过程中也遇到了一下问题。下面一一说明。

配置中的坑
----------

按照项目中的配置起初没有跑起来，没有跑起来的原因是session老是找不到。原因是Shiro的session id老是和系统的session id冲掉，在直接使用内存缓存的时候ok，换成了redis的时候就不行了。
所以我就根据 http://www.cnblogs.com/xguo/p/3209529.html 的提示将 shiro-redis_ 中的配置改成如下内容：

.. code-block:: xml
    :linenos:

    <bean id="wapsession" class="org.apache.shiro.web.servlet.SimpleCookie">
        <constructor-arg name="name" value="WAPSESSIONID"/>
    </bean>

    <!-- redisSessionDAO -->
    <bean id="redisSessionDAO" class="org.crazycake.shiro.RedisSessionDAO">
        <property name="redisManager" ref="redisManager" />
    </bean>

    <!-- sessionManager -->
    <bean id="sessionManager" class="org.apache.shiro.web.session.mgt.DefaultWebSessionManager">
        <property name="sessionDAO" ref="redisSessionDAO" />
        <property name="sessionIdCookie" ref="wapsession"/>
    </bean>

    <!-- cacheManager -->
    <bean id="cacheManager" class="org.crazycake.shiro.RedisCacheManager">
        <property name="redisManager" ref="redisManager" />
    </bean>

这样所有问题就解决了，可以正常的在多机器的情况下登陆，登出了。

性能的坑
--------

正当我高兴的时候发现前台的页面变得非常非常的慢。一次请求搞到了1~2秒，天哪这个要用户怎么可能接受，最起码我自己这儿就无法接受了。找原因去，最后发现是在一次的shiro的认证过程中 他要十几次的访问RedisSessionDAO的doReadSession方法，在doReadSession方法中直接访问redis。 也就是说在一次认证过程中，需要访问redis 十几次，在我的屌丝网络中一次访问redis是需要100ms的，十来次就是1000个ms啊。
所以我决定给这个在内存中加一个简单的缓冲，确保一次认证的过程中只是去redis取一次，最多2次就ok。所以我选用了guava中的Cache，他使用简单，无需配置，适用我这个场合。
所以就有了 pull request https://github.com/alexxiyang/shiro-redis/pull/3 。
这样一来，我们页面的访问速度就一下子回到了200 ~ 300 ms了。这个时间范围用户应该还是可以接受的。

在这里非常感谢alex 贡献了他的项目，感谢aliencode的 《Apache-Shiro+Zookeeper系统集群安全解决方案之会话管理》 一文，帮助我找到了cookie冲突的问题。
另外alex在写这篇博客的时候已经同意将我的代码合并到 shiro-redis_ 分支中去。欢迎大家使用这个项目！






.. _shiro-redis : https://github.com/alexxiyang/shiro-redis
