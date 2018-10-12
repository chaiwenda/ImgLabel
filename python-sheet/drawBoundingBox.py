import os
import xml.etree.ElementTree as ET
import cv2

def xmlRead(xml_path):

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for Object in root.findall('object'):
        bndbox = Object.find('bndbox')
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text

        xmin = int(xmin)
        ymin = int(ymin)
        xmax = int(xmax)
        ymax = int(ymax)

    return xmin, ymin, xmax, ymax
if __name__ == '__main__':
    rootPath = 'F:\\ruijie\\0919_extra_data'
    dstRoot =  'F:\\ruijie\\0919_extra_data_image'
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
            # print(subFilesList)
            # print(totalSubFileNum)
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
                imgXMIN, imgYMIN, imgXMAX, imgYMAX = xmlRead(xmlFilePath)
                print(xmlRead(xmlFilePath))

                font = cv2.FONT_HERSHEY_COMPLEX
                classObjectName = iterRootDir

                # cv2.rectangle(img, (imgXMIN, imgYMIN), (imgXMAX, imgYMAX), (0, 255, 0), 4)
                cv2.rectangle(img, (imgXMIN, imgYMIN), (imgXMAX, imgYMAX), (221, 80, 68), 4)
                cv2.putText(img, classObjectName, (imgXMIN, imgYMIN - 10), font, 2, (0, 0, 255), 1)

                imgFileName = imgFile.split('.')[0]
                imgFileNewName = imgFileName + "_rect.jpg"

                dstImagePath = os.path.join(dstRootDirPath, imgFileNewName)
                cv2.imwrite(dstImagePath, img)


# if __name__ == '__main__':
#     rootPath = 'C:\\Users\Administrator\Desktop\\2018729data\Aji'
#     dstRoot = 'C:\\Users\Administrator\Desktop\\2018729data\Aji_rect'
#     for (rootPath, rootDirName, rootFileName) in os.walk(rootPath):
#
#         for iterRootDir in rootDirName:
#             eachRootDirPath = os.path.join(rootPath, iterRootDir)
#             dstRootDirPath = os.path.join(dstRoot, iterRootDir)
#
#             if not os.path.exists(dstRootDirPath):
#                 os.makedirs(dstRootDirPath)
#
#             subFilesList = os.listdir(eachRootDirPath)
#             totalSubFileNum = len(subFilesList)
#             # vectorOperation = 0
#
#             orgImageNamesList = []
#             xmlNameList = []
#
#             for eachFileIter in range(0, totalSubFileNum, 1):
#                 if subFilesList[eachFileIter].split('.')[1] == 'jpg':
#                     fileName = subFilesList[eachFileIter]
#                     orgImageNamesList.append(fileName)
#                 if subFilesList[eachFileIter].split('.')[1] == 'xml':
#                     xmlName = subFilesList[eachFileIter]
#                     xmlNameList.append(xmlName)
#             if len(orgImageNamesList) != len(xmlNameList):
#                 break
#             for matchFileXmlIndex in range(0, len(orgImageNamesList), 1):
#                 imgFile = orgImageNamesList[matchFileXmlIndex]
#                 xmlFile = xmlNameList[matchFileXmlIndex]
#                 print(imgFile)
#                 print(xmlFile)
#                 imgFilePath = os.path.join(eachRootDirPath, imgFile)
#                 xmlFilePath = os.path.join(eachRootDirPath, xmlFile)
#
#                 img = cv2.imread(imgFilePath)
#                 imgXMIN, imgYMIN, imgXMAX, imgYMAX = xmlRead(xmlFilePath)
#
#                 font = cv2.FONT_HERSHEY_COMPLEX
#                 classObjectName = iterRootDir
#
#                 cv2.rectangle(img, (imgXMIN, imgYMIN), (imgXMAX, imgYMAX), (0, 255, 0), 4)
#                 cv2.putText(img, classObjectName, (imgXMIN, imgYMIN - 10), font, 2, (0, 0, 255), 1)
#
#                 imgFileName = imgFile.split('.')[0]
#                 imgFileNewName = imgFileName + "_rect.jpg"
#
#                 dstImagePath = os.path.join(dstRootDirPath, imgFileNewName)
#                 cv2.imwrite(dstImagePath, img)
