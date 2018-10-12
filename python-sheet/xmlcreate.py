import os
import xml.dom.minidom
"""
function:给xml文件添加两个标注框
"""

read_file = 'F:\\ruijie\\0823_extra_data\caffebag'

for file_name in os.listdir(read_file):
    new_txtname = file_name.split('.')[0]

    # 创建一个空的Dom文档对象
    doc = xml.dom.minidom.Document()
    # 创建根节点，此根节点为annotation
    annotation = doc.createElement('annotation')
    # 将根节点添加到DOm文档对象中
    doc.appendChild(annotation)

    folder = doc.createElement('folder')
    # 内容写入
    folder_text = doc.createTextNode('caffebag')
    folder.appendChild(folder_text)
    annotation.appendChild(folder)

    filename = doc.createElement('filename')
    filename_text = doc.createTextNode(file_name)
    filename.appendChild(filename_text)
    annotation.appendChild(filename)

    path = doc.createElement('path')
    path_text = doc.createTextNode('D:\data\caffebag\\'+file_name)
    path.appendChild(path_text)
    annotation.appendChild(path)

    source = doc.createElement('source')
    databass = doc.createElement('databass')
    databass_text = doc.createTextNode('Unknown')
    source.appendChild(databass)
    databass.appendChild(databass_text)
    annotation.appendChild(source)

    size = doc.createElement('size')
    width = doc.createElement('width')
    width_text = doc.createTextNode('640')
    height = doc.createElement('height')

    height_text = doc.createTextNode('480')
    depth = doc.createElement('depth')
    depth_text = doc.createTextNode('3')
    size.appendChild(width)
    width.appendChild(width_text)
    size.appendChild(height)
    height.appendChild(height_text)
    size.appendChild(depth)
    depth.appendChild(depth_text)
    annotation.appendChild(size)

    segmented = doc.createElement('segmented')
    segmented_text = doc.createTextNode('0')
    segmented.appendChild(segmented_text)
    annotation.appendChild(segmented)

    oj = doc.createElement('object')

    oj_name = doc.createElement('name')
    oj_name_txt = doc.createTextNode('caffebag')
    oj_name.appendChild(oj_name_txt)
    oj.appendChild(oj_name)

    oj_pose = doc.createElement('pose')
    oj_pose_txt = doc.createTextNode('Unspecified')
    oj_pose.appendChild(oj_pose_txt)
    oj.appendChild(oj_pose)

    oj_truncated = doc.createElement('truncated')
    oj_truncated_txt = doc.createTextNode('0')
    oj_truncated.appendChild(oj_truncated_txt)
    oj.appendChild(oj_truncated)

    oj_difficult = doc.createElement('difficult')
    oj_difficult_txt = doc.createTextNode('0')
    oj_difficult.appendChild(oj_difficult_txt)
    oj.appendChild(oj_difficult)

    oj_bndbox = doc.createElement('bndbox')
    oj_bndbox_xmin = doc.createElement('xmin')
    oj_bndbox_xmin_txt = doc.createTextNode('216')
    oj_bndbox_xmin.appendChild(oj_bndbox_xmin_txt)
    oj_bndbox.appendChild(oj_bndbox_xmin)

    oj_bndbox_ymin = doc.createElement('ymin')
    oj_bndbox_ymin_txt = doc.createTextNode('291')
    oj_bndbox_ymin.appendChild(oj_bndbox_ymin_txt)
    oj_bndbox.appendChild(oj_bndbox_ymin)

    oj_bndbox_xmax = doc.createElement('xmax')
    oj_bndbox_xmax_txt = doc.createTextNode('283')
    oj_bndbox_xmax.appendChild(oj_bndbox_xmax_txt)
    oj_bndbox.appendChild(oj_bndbox_xmax)

    oj_bndbox_ymax = doc.createElement('ymax')
    oj_bndbox_ymax_txt = doc.createTextNode('385')
    oj_bndbox_ymax.appendChild(oj_bndbox_ymax_txt)
    oj_bndbox.appendChild(oj_bndbox_ymax)

    oj.appendChild(oj_bndbox)
    annotation.appendChild(oj)
    # 写入xml文本文件中
    fp = open('F:\\ruijie\\0823_extra_data\caffebag\\%s.xml' % new_txtname, 'w+')
    doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding='utf-8')
    fp.close()