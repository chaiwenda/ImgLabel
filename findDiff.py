import os

rootPath = 'C:\\Users\Administrator\Desktop\data'

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
            print(localValue)
