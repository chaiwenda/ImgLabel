# date:2018/8/23 9:39
# -*- coding: utf-8 -*-
#author;cwd
"""
function:建立xml文件模板,包含两个标注框
"""
import sys, os

rootPath = 'F:\\ruijie\\0823_extra_data'

for (rootPath, rootDirName, rootFileName) in os.walk(rootPath):

    for iterRootDir in rootDirName:
        print(rootDirName)
        print(rootFileName)
        eachRootDirPath = os.path.join(rootPath, iterRootDir)
        subFilesList = os.listdir(eachRootDirPath)
        print(subFilesList)
        filePath = eachRootDirPath
        for item in subFilesList:

            xmlfilename = item.split(".")[0] + ".xml"
            xmlfilePath =  os.path.join(filePath, xmlfilename)
            print(xmlfilename)
            print(xmlfilePath)

            XmlModel = "<annotation>\n" \
                       "    <folder>caffebag</folder>\n" \
                       "    <filename>" + xmlfilename.split('.')[0] + ".jpg" + "</filename>\n" \
                                                 "    <path>" + xmlfilePath.split('.')[0] + ".jpg" + "</path>\n" \
                                                                       "    <source>\n" \
                                                                       "        <database>Unknown</database>\n" \
                                                                       "</source>\n" \
                                                                       "    <size>\n      <width>640</width>\n      <height>480</height>\n      <depth>3</depth>\n</size>\n" \
                                                                       "    <segmented>0</segmented>\n     <object>\n" \
                                                                       "        <name>" + iterRootDir + "</name>\n" \
                                                                       "        <pose>Unspecified</pose>\n" \
                                                                       "        <truncated>0</truncated>\n" \
                                                                       "        <difficult>0</difficult>\n" \
                                                                       "        <bndbox>\n        <xmin>441</xmin>\n        <ymin>239</ymin>\n          <xmax>506</xmax>\n          <ymax>333</ymax>\n      </bndbox>\n     </object>\n     <object>\n        <name>" + iterRootDir+ "</name>\n        <pose>Unspecified</pose>\n        <truncated>0</truncated>\n        <difficult>0</difficult>\n        <bndbox>\n            <xmin>447</xmin>\n            <ymin>253</ymin>\n            <xmax>500</xmax>\n            <ymax>307</ymax>\n        </bndbox>\n    </object>\n</annotation>\n"



            with open(xmlfilePath, 'w') as f:  # 设置文件对象
                f.write(XmlModel)  # 将字符串写入文件中




        # filenamePath = os.path.join(filePath, filename)
        # filenamePath = os.path.join(filePath, filename)


