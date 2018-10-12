import os

"""
function：修改文件名
file_class_path：类文件根目录
注：路径后加“\\”
"""

file_class_path = 'C:\\Users\Administrator\Desktop\\7_29_已标注\\7类\zhongwotizhinengliang\\'

file_name = os.listdir(file_class_path)
for temp in file_name:
    # new_name = temp +'_new'
    if os.path.splitext(temp)[1] == '.jpg':
        new_name = os.path.splitext(temp)[0]+'_new'+'.jpg'
        print('jpg file rename:'+new_name)
    if os.path.splitext(temp)[1] == '.xml':
        new_name = os.path.splitext(temp)[0]+'_new'+'.xml'
        print('xml file rename:'+new_name)
    os.rename(file_class_path + temp, file_class_path + new_name)