import os

outputdir = "F:\python_projects\labelImg-master\labelImg-master\image\\145456_367803573_1_500_282 - 副本 - 副本 (2).jpg"
index = outputdir.rfind('\\')
print('\下标是')
print(index)
fname = outputdir[index+1:]
fpath = outputdir[:index+1]
index1 = fname.rfind('.')
fname_no_suffix = fname[:index1]
print("输出照片名称")
print(fname)

print("输出当前绝对路径")
print(fpath)

print("输出照片名称不带后缀")
print(fname_no_suffix)