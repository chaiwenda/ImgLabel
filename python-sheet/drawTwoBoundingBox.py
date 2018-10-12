# date:2018/9/8 20:48
# -*- coding: utf-8 -*-
#author;cwd
"""
function:画两个矩形框，红色框代表标的不对，绿色框代表正确标发
    rootPath = 'F:\\ruijie\\0907_test_data'  =>二级根目录地址
    dstRoot = 'F:\\ruijie\\0908_extra_image_data'  =>储存图片文件夹地址
"""
import os
import xml.etree.ElementTree as ET
import cv2

def xmlRead(xml_path):

    tree = ET.parse(xml_path)
    root = tree.getroot()
    xml_lists = []
    for Object in root.findall('object'):
        bndbox = Object.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        xml_index_lists = [xmin, ymin, xmax, ymax]
        xml_lists.append(xml_index_lists)

    return xml_lists

if __name__ == '__main__':
    rootPath = 'F:\\ruijie\\0907_test_data'
    dstRoot = 'F:\\ruijie\\0908_extra_image_data'
for (rootPath, rootDirName, rootFileName) in os.walk(rootPath):
        for iterRootDir in rootDirName:
            eachRootDirPath = os.path.join(rootPath, iterRootDir)
            dstRootDirPath = os.path.join(dstRoot, iterRootDir)

            if not os.path.exists(dstRootDirPath):
                os.makedirs(dstRootDirPath)
            # 文件列表
            subFilesList = os.listdir(eachRootDirPath)
            # jpg + xml 文件
            totalSubFileNum = len(subFilesList)
            # vectorOperation = 0

            orgImageNamesList = []
            xmlNameList = []

            for eachFileIter in range(0, totalSubFileNum, 1):
                if subFilesList[eachFileIter].split('.')[1] == 'jpg':
                    fileName = subFilesList[eachFileIter]
                    orgImageNamesList.append(fileName)
                if subFilesList[eachFileIter].split('.')[1] == 'xml':
                    xmlName = subFilesList[eachFileIter]
                    xmlNameList.append(xmlName)
            if len(orgImageNamesList) != len(xmlNameList):
                break
            for matchFileXmlIndex in range(0, len(orgImageNamesList), 1):
                imgFile = orgImageNamesList[matchFileXmlIndex]
                xmlFile = xmlNameList[matchFileXmlIndex]
                print(imgFile)
                print(xmlFile)
                imgFilePath = os.path.join(eachRootDirPath, imgFile)
                xmlFilePath = os.path.join(eachRootDirPath, xmlFile)

                img = cv2.imread(imgFilePath)
                index_lists = xmlRead(xmlFilePath)
                print(len(index_lists))
                color_lists = [[0, 0, 255], [0, 252, 124]]
                text_lists = ["No", "Yes"]
                for i in range(0, len(index_lists), 1):
                    font = cv2.FONT_HERSHEY_COMPLEX
                    cv2.rectangle(img, (index_lists[i][0], index_lists[i][1]), (index_lists[i][2], index_lists[i][3]),
                                  (color_lists[i][0], color_lists[i][1], color_lists[i][2]), 4)
                    if i == 1:
                        cv2.putText(img, text_lists[i], (index_lists[i][0], index_lists[i][1] - 10), font, 3, (color_lists[i][0], color_lists[i][1], color_lists[i][2]), 1)

                    imgFileName = imgFile.split('.')[0]
                    imgFileNewName = imgFileName + "_rect.jpg"

                    dstImagePath = os.path.join(dstRootDirPath, imgFileNewName)
                    cv2.imwrite(dstImagePath, img)


