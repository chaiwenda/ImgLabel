# import os
#
# outputdir = "F:\python_projects\labelImg-master\labelImg-master\image\\145456_367803573_1_500_282 - 副本 - 副本 (2).jpg"
# index = outputdir.rfind('\\')
# print('\下标是')
# print(index)
# fname = outputdir[index+1:]
# fpath = outputdir[:index+1]
# index1 = fname.rfind('.')
# fname_no_suffix = fname[:index1]
# print("输出照片名称")
# print(fname)
#
# print("输出当前绝对路径")
# print(fpath)
#
# print("输出照片名称不带后缀")
# print(fname_no_suffix)
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QDialog, QLineEdit, QTextBrowser,
        QVBoxLayout)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)
        self.lineedit.setText('')

if __name__=="__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()