Grails代码阅读
============================

:date: 2015-4-05 10:20
:modified: 2015-4-05 18:40
:tags: Grails, CodeRead
:category: Grails
:authors: Jet Geng
:summary: 代码阅读


启动
----

Grails启动相关的内容是在 grails-bootstrap 中体现的。
所有命令行的启动都是通过GrailsScriptRunner来完成。本质上找到对应的脚本，然后去执行。executeCommand来执行脚本。





