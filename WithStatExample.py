'''
with语句使用示例
'''
# -*- coding: utf-8 -*-
class fileLoader:
    def __init__(self,path):
        print("init")
        self.path = path;
    def __enter__(self):
        print("enter")
        self.file = open(self.path,"r");
        return  self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
        print(str(exc_type)+"::::::"+str(exc_val)+":::::"+str(exc_tb))

    def showContext(self):
        print(self.file.read())

# with fileLoader("./test.txt") as fr:
#     fr.showContext()

with fileLoader("./classExample.py") as fr:
    fr.showContext()