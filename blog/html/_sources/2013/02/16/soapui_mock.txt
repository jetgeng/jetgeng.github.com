用SoapUI mock Web服务
======================
最近工作大量使用三方的Web Service（以下简称WS）。三方的WS时好时坏。让人很是郁闷，所以就动了自己按照三方提供的wsdl自己实现同样接口的WS。其实这就是Mock。 简单google了一下发现 `SoapUI <http://www.soapui.org/Service-Mocking/creating-dynamic-mockservices.html>`_ 已经具有这样的功能，而且很容易上手。毫不犹豫的用起来。

创建动态的WS mock
------------------------

我们的目标是根据一个wsdl文件创建一个WS mock。WS client可以方法这个WS mock，并且能产生动态的相应。
在开始前我们需要如下材料：

 #. JDK， 建议使用1.5向上版本。
 #. SoapUI 4.5.1版本
 #. 一个wsdl文件。我使用的wsdl文件在

好了，准备好上述的内容我们就开始创建WS mock。
首先打开SoapUI。 通过File菜单中的new project新建一个项目。

.. image:: ../../../static/images/soap-newproject.jpg



.. author:: Jet Geng 
.. categories:: WS 
.. tags:: Java Groovy
.. comments::
