Kid Capture开发手记
============================

缘起
------------------------------------------------------------    
我四岁的儿子和他10岁的表哥迷上了我的电脑，只要我不用就和他哥跑到电脑前。随后就会传来一阵阵的狂笑。我过去一看发现他们抱着Photo Booth狂拍照片，狂拍视屏。被那些加上各种各样效果的视屏逗的开心死了。
这个时候我就在想我自己能否做一个这种小东西呢？让儿子在他妈妈的 **瘟都死** （Windows）上也能用呢？
整理整理思路就动手做吧！

需求
------------------------------------------------------------    
虽然是个小东西，但是也要简单列举一下需求。以确定开发的边界。
 1. 通过摄像头获取图像信息。显示到主界面上。
 2. 提供三个功能按钮

    **开始录制视屏**
        点击后就开始将摄像头获取的图片信息以视频流的形式保存成一个文件。同时还需要记录下麦克风的声音。保存成文件
    **停止录制**
        停止录制的过程，将声音文件和视频文件合并成一个小电影
    **拍照**
        将摄像头的当前帧保存成文件

第一个版本先做这么多吧！关于效果部分后续在跟进

技术方案
------------------------------------------------------------    
由于我预定的目标平台是 **瘟都死**  又不想使用笨重的Visual Studio。
所以决定采用如下的工具
 #. 开发语言-- Python_
 #. 图形界面框架 -- wxPython_
 #. 图像采集和分析框架 -- OpenCV_
 #. 声音采集工具  -- PyAudio_

图像采集
------------------------------------------------------------    

图像采集说白了就是从摄像头读取图像信息。在微软家有Direct.Show 可以用。从CodeProject网站上可以找到大量的示例，不是C#就是VB。 当然通过Python也可以调用，只是要求系统上一定要有Direct。所以放弃。最后在Youtube上看到一老外用10行代码完成了视屏采集。为之一动，对自己说就用他吧！他就是OpenCV。

.. code-block:: python
    :linenos:

    #!/usr/bin/python
    # -*- coding: utf-8 -*-
    
    import cv2.cv as cv
    import cv2
    
    capture = cv.CaptureFromCAM(0)
    
    cv.NamedWindow("camera", 1)
    
    while True:
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera", img)
        k = 0xFF & cv.WaitKey(10);
        if k == 27:
            break

#. 4,5行导入OpenCV的包
#. 7打开摄像头，并开始读取frame
#. 11 ~ 13 读取摄像头的数据帧，并显示到窗体中。
#. 15 ~ 16 判断有没有用户输入，如果是 esc键就退出。

 上面的代码就是视屏捕捉的所有核心！超级简单吧！不过有个问题上面的代码只能使用 OpenCV_ 自己的图像界面，而且他的并不能集成到其他框架中来。所以要对他他做写改动才可以。

 在他的官方网站上找到了一个例子

初次接触PyAudio
=================

前两天无意间PyAudio，当时没觉得怎么地。今天拿过来练了练。发现这个小东西还真的不错。只需要简单的几行代码就可以完成录音和播放wav的功能。而且他还是跨平台的，在WinXp和Linux下运行良好（遗憾的是在Mac OS Lion下编译没通过）。

下面这个代码来源于实现了录音功能。 http://hyry.dip.jp:8000/pydoc/wave_pyaudio.html#pyaudio 。

.. code-block:: python 
    
    # -*- coding: utf-8 -*-
    from pyaudio import PyAudio, paInt16 
    import numpy as np 
    from datetime import datetime 
    import wave 
    
    
    # 将data中的数据保存到名为filename的WAV文件中
    def save_wave_file(filename, data): 
        wf = wave.open(filename, 'wb') 
        wf.setnchannels(1) 
        wf.setsampwidth(2) 
        wf.setframerate(SAMPLING_RATE) 
        wf.writeframes("".join(data)) 
        wf.close() 
    
    
    
    NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
    SAMPLING_RATE = 8000    # 取样频率
    LEVEL = 1500            # 声音保存的阈值
    COUNT_NUM = 20          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
    SAVE_LENGTH = 8         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
    
    # 开启声音输入
    pa = PyAudio() 
    stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True, 
                    frames_per_buffer=NUM_SAMPLES) 
    
    save_count = 0 
    save_buffer = [] 
    
    while True: 
        # 读入NUM_SAMPLES个取样
        string_audio_data = stream.read(NUM_SAMPLES) 
        # 将读入的数据转换为数组
        audio_data = np.fromstring(string_audio_data, dtype=np.short) 
        # 计算大于LEVEL的取样的个数
        large_sample_count = np.sum( audio_data > LEVEL ) 
        print np.max(audio_data) 
        # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
        if large_sample_count > COUNT_NUM: 
            save_count = SAVE_LENGTH 
        else: 
            save_count -= 1 
    
        if save_count < 0: 
            save_count = 0 
    
        if save_count > 0: 
            # 将要保存的数据存放到save_buffer中
            save_buffer.append( string_audio_data ) 
        else: 
            # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻
            if len(save_buffer) > 0: 
                filename = datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav" 
                save_wave_file(filename, save_buffer) 
                save_buffer = [] 
                print filename, "saved" 
        content



.. _Python: http://python.org/
.. _wxPython: http://wxpython.org/
.. _OpenCV: http://opencv.org/
.. _PyAudio: http://people.csail.mit.edu/hubert/pyaudio/
.. author:: JetGeng 
.. categories:: Python 
.. tags:: Python 
.. comments::
