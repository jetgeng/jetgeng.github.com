Angularjs中的动态切换服务
=============================

:date: 2015-3-28 17:39
:tags: AngularJs
:category: 前端


需求
----

近期在用Angularjs做点小东西。在使用的过程中遇到如下的需求。
我想把运行环境分成开发（dev），测试(test), 线上(prod)这三个环境。在这三个不同的环境中有一些配置行为是不一样的。比如获取数据的地址了，登陆的方法等等。


解题思路
--------

由于有点Spring的使用经验，第一反应就是想动态替换Service。

一般情况下在controller中注入服务，采用如下形式。

.. code-block:: javascript

     angular.moule('someMoule',[])
     .controller('someController',function (someService){
         someService.doSomething();
     }

如何动态的换掉someService呢？经过一番折腾以后，没有找到了合适的方法。

所以穷极生变以后想到采用代理的方式解决这个问题。
于是有了下面的解决方法。

解法
----

最终的解法是采用代理的方式。具体的结构如下：

.. code-block:: javascript

     angular.moule('serviceMoule',[])
     .factory('someService',function (devSomeService,betaSomeService, prodSomeService){

         if(env === "dev"){
             return devSomeService;
         }
         if(env === "beta"){
             return betaSomeService;
         }
         if(env === "prod"){
             return prodSomeService;
         }


     })
     .factory('devSomeService', function(){
         var doSomething = function(){
             console.log(" i am in dev env");
         }
         return {
             doSomething: doSomething
         }
     })
     .factory('betaSomeService', function(){
         var doSomething = function(){
             console.log(" i am in dev env");
         }
         return {
             doSomething: doSomething
         }
     })
     .factory('prodSomeService', function(){
         var doSomething = function(){
             console.log(" i am in dev env");
         }

         return {
             doSomething: doSomething
         }
     })


这样使用的时候直接注入someService 这个服务。最终这个服务将会根据不同的开关来代理devSomeService, betaSomeService, prodSomeService 其中的一个。

这个方法有点土，不过可以工作。如果你有什么更好的办法，欢迎指教！ 谢谢！
