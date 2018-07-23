import os
import xml.etree.ElementTree as ET

def xmlRead(xml_path):

    tree = ET.parse(xml_path)
    root = tree.getroot()

    for Object in root.findall('object'):
        objectName = Object.find('name').text


    return objectName

def xmlWrite(xml_path, ObjectName, xml_outputPath):
    tree = ET.parse(xml_path)
    root = tree.getroot()


    for Object in root.findall('object'):

        objectName = Object.find('name')
        objectName.text = ObjectName

    tree.write(xml_outputPath)

srcRoot = 'F:\QtPython\Data\data2\QingNingShui'
# dstRoot = 'C:\\Users\\R09649\\Desktop\\ChangeXml'
if __name__ == '__main__':
    for (rootPath, rootDirName, rootFileName) in os.walk(srcRoot):

        for iterRootDir in rootDirName:

            eachRootDirPath = os.path.join(rootPath, iterRootDir)

            subFilesList = os.listdir(eachRootDirPath)
            iterLength = len(subFilesList)

            for eachFileIter in range(0, iterLength, 1):

                filePreffix = subFilesList[eachFileIter].split('.')[1]
                if filePreffix == 'xml':
                    xmlFileName = subFilesList[eachFileIter]
                    xmlOrgPath = os.path.join(eachRootDirPath, xmlFileName)

                    if xmlRead(xmlOrgPath) != iterRootDir:
                        # xmlDstPath = os.path.join(dstRootDirPath, xmlFileName)
                        print(xmlFileName)
                        newName = iterRootDir
                        xmlWrite(xmlOrgPath, newName, xmlOrgPath)
