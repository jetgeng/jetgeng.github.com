使用Gorm引起的一次奔溃
######################

:date: 2016-3-5 16:51
:tags:
:category: GORM
:slug: crashstory
:summary: 使用GORM引起的奔溃
:status: draft


案发第一现场
------------

前方告急，系统不能登录。迅速打开日志查看，是其中一个系统无法获取到数据库连接，JVM内存溢出（传说中的OOM）。我们的数据使用的postgresql。 凭感觉冲到数据库服务器上去看看数据库什么情况。使用

.. code-block:: bash

   ps aux | grep 'post'

发现输出的结果是很多有很多 `in transaction`. 啥请求啊，长时间没有结束。使用psql连接进数据库。使用如下sql

.. code-block:: sql

   SELECT * FROM pg_stat_activity WHERE dataname= '${database name}' and state like '%transaction';

结果发现被查询的是用户表，要命的居然没有加上任何查询条件。查询sql如下：

.. code-block:: sql

   select this_.id as id1_2_0_, 
          this_.version as version2_2_0_, 
          this_.account_expired as account3_2_0_, 
          this_.account_locked as account4_2_0_,
          this_.date_created as date5_2_0_, 
          this_.email as email8_2_0_, 
          this_.id_no as id11_2_0_, 
          this_.mobile as mobile12_2_0_,
          this_."password" as passwor13_2_0_, 
  from users this_


追踪开始
--------

看到上面的情况第一反应是不是我的Users在什么地方调用了 Users.list() 这样的语句。然后去执行上面的sql。 找遍了所有系统，没有找到这样的代码。
怎么回事呢？通过执行顺序和log，终于发现如下的一行代码是罪魁祸首。

.. code-block:: java

   if( 
    user.properties.containsKey("realName")){
    //Do something
        }

user 是User对象的一个实例。就是因为使用了 user.properties 这个属性就触发了获取全部数据的内容。











