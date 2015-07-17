在redhat中安装postgresql
============================

:date: 2015-4-11 10:20
:tags: sql
:category: DataBase
:authors: Jet Geng
:summary: 安装数据库


开始 http://people.planetpostgresql.org/devrim/index.php?/archives/80-Installing-and-configuring-PostgreSQL-9.3-and-9.4-on-RHEL-7.html 安装数据库。

要注意特定的系统的版本

http://yum.postgresql.org/9.4/redhat/rhel-5.4-x86_64/pgdg-redhat94-9.4-1.noarch.rpm

查看linux是32还是64？

.. code-block:: bash

   file /bin/ls

下面去修改/etc/yum.repo.d 中的内容

.. code-block:: bash


   sudo yum install postgresql94.x86_64 postgresql94-contrib.x86_64 postgresql94-debuginfo.x86_64 postgresql94-devel.x86_64 postgresql94-docs.x86_64 postgresql94-libs.x86_64 postgresql94-server.x86_64

/sbin 必须放到path中。


.. code-block:: bash

   sudo service postgresql-9.4 initdb //初始化db
   sudo service postgresql-9.4 start //启动数据库

   \c database_name //切换数据库

用新用户登录数据库：postgresql Peer authentication failed for user

http://stackoverflow.com/questions/18664074/getting-error-peer-authentication-failed-for-user-postgres-when-trying-to-ge

postgresql 的认证方式有多种方式：

#. peer登录，这个就是和操作系统的用户一样。
#. md5 就是通过用户名和密码登录。
