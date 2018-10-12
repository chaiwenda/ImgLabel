import os

"""
查询jpg与xml文件是否一一对应 
"""

rootPath = 'F:\\ruijie\\1010_extra_data'

if __name__ == '__main__':
    # start = time.time()
    for (rootPath, rootDirName, rootFileName) in os.walk(rootPath):

        for iterRootDir in rootDirName:

            eachRootDirPath = os.path.join(rootPath, iterRootDir)
            subFilesList = os.listdir(eachRootDirPath)

            totalSubFileNum = len(subFilesList)

            orgImageNamesList = []
            xmlNameList = []

            for eachFileIter in range(0, totalSubFileNum, 1):

                # if subFilesList[eachFileIter].find('.jpg'):
                if subFilesList[eachFileIter].split('.')[1] == 'jpg':
                    fileName = subFilesList[eachFileIter].split('.')[0]
                    orgImageNamesList.append(fileName)
                if subFilesList[eachFileIter].split('.')[1] == 'xml':
                    xmlName = subFilesList[eachFileIter].split('.')[0]
                    xmlNameList.append(xmlName)
                if subFilesList[eachFileIter].split(".")[1] != 'jpg' and subFilesList[eachFileIter].split(".")[1] != 'xml':
                    errorFile = subFilesList[eachFileIter].split('.')[0]
                    print(errorFile)

            localValue = list(set(set(orgImageNamesList).difference(set(xmlNameList))).union(set(set(xmlNameList).difference(set(orgImageNamesList)))))
            if len(localValue) != 0:
                for item in localValue:
                    print("==================")
                    print(item)
                    print("==================")
                print("[")
                for item in localValue:
                    index = item.rfind('_')
                    delete_file_jpg_name = str(eachRootDirPath) + "\\" + str(item) + ".jpg"
                    delete_file_xml_name = str(eachRootDirPath) + "\\" + str(item) + ".xml"
                    if os.path.exists(delete_file_jpg_name):
                        os.remove(delete_file_jpg_name)
                        print(delete_file_jpg_name),
                    if os.path.exists(delete_file_xml_name):
                        os.remove(delete_file_xml_name)
                        print(delete_file_xml_name),
                print("]")
            else:
                print("[]")

