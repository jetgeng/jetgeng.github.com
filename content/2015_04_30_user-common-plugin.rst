微信用户的设计
##################

:date: 2015-4-30 18:03
:tags:
:category: 设计
:slug: user-common-plugin
:summary:
:status: draft

让客户端能够接受微信的validate
--------------------------------------

当前的问题
^^^^^^^^^^

对于存在于数据库的用户，没有问题。但是现在微信中存在，但是在我们的数据库中不存在的用户，怎么办。 这个时候用户一定已经有了。
我们只是需要让他做关联。要做的内容：

#. 修改spring-security-cas的内容。要求能够创建新的UserDetail.  现在使用的是  GormUserDetailsService
#. 通过新建不同的Authentication 来处理这件事情。


当前系统中支持三种class：

.. uml::

    class UsernamePasswordAuthenticationToken{
    }

    class CasAuthenticationToken {
    }

    class CasAssertionAuthenticationToken {
    }

    class UserDetailsProxyService {
        
    }

    

现在最核心的问题是AbstractCasAssertionUserDetailsService 这个类，也就是获取用户信息的方法。如果我只是换取一个这个方法，就解决了。

这么一来就简单了。只需要建立一个proxy这样的东西就好了。
我如何来调试这个呢？我们的cas使用的是一个叫做 AssertionImpl 这样的东西。







