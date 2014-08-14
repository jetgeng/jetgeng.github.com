Git使用小技巧
==============
使用git也有段时间了。其中遇到一些问题，google半圈找到一些觉得不错的技巧记录在此。防止自己会忘掉。


标签相关
--------

好不容易创建将手头上的工作告一段落了。可以提供给用户使用了。为了以后很方便的找到这个版本，所以就打一个tag啊。迫不及待的敲了下面的命令。

.. code-block:: bash

    git tag  -a cool_tagname -m 'cool comment'
    git push origin -- tag

心里说不出的畅快啊。终于完成了这些活。
稍等，qa又测试出bug了。你这个tag上的内容还不能发布。修改吧。经过一堆修改。git add , git commit 操作以后问题搞定了。
这一回是真的，真的可以提交了。可以打tag了。但是那个那么好的，和功能那么匹配的tag name已经被占用了。把他删除掉，再加一下就好了。
所以我们需要如下的操作：

.. code-block:: bash
   :linenos:

   git push --delete origin cool_tagname
   git tag -a cool_tagname -m ''
   git push origin --tag
   or
   git push refs/tags/release-1.0:refs/tags/release-1.0

代码说明:

1. 第一行 删除远端原来的tag
1. 第2~3行 重新创建并推送到远端
1. 第5行 另外一种推送方式。相对底层的推送方式。
好了，打完收工。tag就修正好。

查看标签创建的时间
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    git log --tags --simplify-by-decoration --pretty="format:%ci %d" 

输出结果如下

.. code-block:: bash

   git log --tags --simplify-by-decoration --pretty="format:%ci %d"
   2014-01-18 22:27:00 +0800  (tag: v1.0.2)
   2013-11-26 00:09:57 +0800  (tag: v1.0.1)



分支相关
--------
创建分支
^^^^^^^^

从当前分支创建一个新分支：

.. code-block:: bash

    git checkout -b BranchName

从远端分支创建一个新分支

.. code-block:: bash

   git checkout -b <branch> --track <remote>/<branch>
   git checkout -b <branch> <remote>/<branch>


删除分支
^^^^^^^^

删除本地分支：

.. code-block:: bash

   git branch -d <branch>

删除远程分支

.. code-block:: bash

   git push <remote> --delete <branch>

推送代码到远端
--------------

.. code-block:: bash

   #推送tracked的分支
   git push <remote> 
   #推送当前分支到远端特定分支
   git push <remote> <remote_branch>
   #将本地特定分支推送到远端特定分支
   git push <remote <local_branch>:<remote_branch>






















.. author:: Jet Geng
.. categories:: none
.. tags:: Git 
.. comments::
