Grails从2.2升级到2.3.3遇到的问题
============================================================

Debug
----------

升级到2.3 以后我就找不到grails-debug 这个命令了。后进过查询发现原来是被 ``grails -debug`` 这个参数替代了。是要了这个参数以后又遇到一个问题。就是需要通过Remote Debug 的方式连接进去才可以。但是不管咋地都不在断点处停下来。真的让人抓狂。

最后通过这个一个老外的一段话给解决了

 
    In Intellij  go to "Run / Edit Configurations", click + then "Remote" and name it whatever  you want (example "Grails Remote") then press ok.
    Then from the command line do:
    grail run-app --debug-fork
    Attach your debugger by running your "Grails Remote" config. Done.

原来是需要使用 grails run-app --debug-fork 命令来做。解了，亲测！





.. author:: default
.. categories:: none
.. tags:: none
.. comments::
