使用Karam和Jasmine对前后分离的项目做集成测试
############################################

:date: 2015-11-12 16:24
:tags:
:category: 前端
:slug:
:summary:
:status: draft



背景
--------

由于我们系统严格采用前后分离的方法来做的。后台提供的服务其实就是一个个的通过http暴露出来的服务。所以前台和后台交互的方式其实就是这些http服务。
为了确保这些服务是完全可用的，所以需要对这些服务进行测试。测试的方式有多种，比如后台程序员自己写单元测试。另外就是模拟接口真实使用场景，通过发送http请求对这些接口进行测试。
我要介绍的是后面这种情况。他有如下优点：

 * 完全模拟接口使用场景，根据真实性.
 * 可以成为前后端程序员交互的依据。（这些测试后端程序员写）

使用的技术以及环境配置
--------------------------------

具体使用了如下内容：

 1. Angularjs_ 我们前端开发框架使用的是这个。
 1. Grunt_ 项目构建工具，类似于java世界的ant,gradle.
 1. Jasmine_ JavaScript 世界的一个 行为测试框架
 1. Karam_ JavaScript 的一个测试运行器.

环境安装
^^^^^^^^^^^^^^^^^

预先加上开发机器上已经安装好了node.js。 开始安装所需要的内容. 进入你所需要的测试的项目所处的目录中。运行如下代码：


.. code-block:: bash

    npm install -g grunt-cli
    npm install karma --save-dev
    npm install karma-coverage karma-jasmine --save-dev
    npm install karma-html-reporter jasmine karma-chrome-launcher karma-phantomjs-launcher --save-dev
    npm install grunt-karma --save-dev



配置Gruntfile
^^^^^^^^^^^^^^^^^





.. _Karam: http://karma-runner.github.io/
.. _Jasmine: http://jasmine.github.io/
.. _Grunt: http://gruntjs.com/
.. _Angularjs: https://angularjs.org/
