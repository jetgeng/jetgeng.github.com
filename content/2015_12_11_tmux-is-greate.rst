在ssh session断开后继续运行命令
###################################

:date: 2015-12-11 17:23
:tags:
:category: ops
:slug: tmux-is-greate
:summary: linux常用工具之tmux


前因
---------------

在工作的过程中经常会遇到需要在远端服务器上执行一些耗时长，干预少的任务。在先前通过ssh连接进远端服务器，但是一旦ssh session断开以后，在这个session中的进程将会全部会被杀死。
这就意味着在ssh session中执行的命令，将会随着ssh session的终结而终结。为了解决这个 会话断开_ 的问题。我们找到了tmux。


在该场景下的使用方法
------------------------

通过ssh登录进远程的机器。打开tmux，完成你的个各项操作。
在这个时候就是你断开了。当你重新连接进改服务器的时候，只要使用tmux attach命令，你就得到了你刚才工作的环境。这样会大大提高工作效率。

如何学习tmux
----------------

如果想熟练使用还是需要花一点时间简单学习一下。下面简单罗列一下个人觉得不错的资料，供你参考：

1. `The Tao of tumx <http://tmuxp.readthedocs.org/en/latest/about_tmux.html>`_
1. `tmux官网 <https://tmux.github.io/>`_


.. _会话断开: http://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session
