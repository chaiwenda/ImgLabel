# date:2018/9/6 15:26
# -*- coding: utf-8 -*-
#author;cwd
"""
function:
"""
#!/usr/bin/env python
#coding:utf-8

'''
Created on 2016年6月9日

@author: lei.wang
'''
import os
pathB = "F:\\ruijie\PartThree\StarBucksDoubleShot\StarBucksDoubleShot"
pathA = "F:\\ruijie\PartThree\checked\StarBucksDoubleShot"
def diff(listA,listB):
    # #求交集的两种方式
    retA = [i for i in listA if i in listB]
    return retA
    # retB = list(set(listA).intersection(set(listB)))

    print("retA is: ",len(retA))
    # print("retB is: ",retB)
    #
    # #求并集
    # retC = list(set(listA).union(set(listB)))
    # print("retC1 is: ",retC)

    #求差集，在B中但不在A中
    # retD = list(set(listB).difference(set(listA)))
    # print("retD is: ", retD)
    # return retD


    # retE = [i for i in listB if i not in listA]
    # return retE
    # print("retE is: ",retE)


def main():
    listsB = os.listdir(pathB)
    listsA = os.listdir(pathA)
    lists = diff(listsA,listsB)
    # print(len(lists))
    for item in lists:
        print(item)
        os.remove(os.path.join(pathB,item))

if __name__ == '__main__':
    main()