# date:2018/8/23 14:50
# -*- coding: utf-8 -*-
#author;cwd
"""
function:检验是否有两个标注框，异常的输出并删除
"""
import sys, os

rootPath = 'F:\\ruijie\\0907_test_data'

for (rootPath, rootDirName, rootFileName) in os.walk(rootPath):
    # print(rootDirName)
    for iterRootDir in rootDirName:
        print("当前在" + iterRootDir + "文件夹下")
        eachRootDirPath = os.path.join(rootPath, iterRootDir)
        subFilesList = os.listdir(eachRootDirPath)
        xmlLists = [] # jpg文件列表
        for item in subFilesList:
            if item.split(".")[1] == "xml":
                xmlLists.append(item)
        # print(xmlLists)
        for iter in xmlLists: # 遍历每个xml文件
            xmlpath = os.path.join(eachRootDirPath, iter)
            # print(xmlpath)
            f = open(xmlpath)
            number = 0
            for line in f:
                if "<object>" in line:
                    number += 1
            if number != 2:
                print(iter + "文件异常")
                f.close()

                XmlFilePath = os.path.join(eachRootDirPath, iter)
                ImgFilePath = os.path.join(eachRootDirPath, iter.split('.')[0] + '.jpg')
                os.remove(ImgFilePath)
                os.remove(XmlFilePath)















