#!/usr/bin/env python
# encoding: utf-8

import bash

rstFiles = bash.bash('find 2014  -name \'*.rst\'')

filesInArray = rstFiles.stdout.split('\n')
for fileName in filesInArray:
    fileNameArray = fileName.split('/')
    if len(fileNameArray) == 4:
        copyCmd = 'cp %s  %s/%s_%s_%s_%s' % (
            fileName,
            '/Users/jet/Code_Repo/JetNewBlog/content',
            fileNameArray[0], fileNameArray[1], fileNameArray[2], fileNameArray[3])
        print copyCmd
        bash.bash(copyCmd)
