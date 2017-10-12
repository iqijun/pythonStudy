# -*- coding: utf-8 -*-
#定义一个class

class Demo:
    #定义成员变量,类似于java中的静态变量，所有的对象共享该属性的值
    address = "北京";
    #类似于构造函数
    def __init__(self):
        self.name = "cruise";
    def getInfo(self):
        print("name:"+self.name+";地址："+ self.address)
    #定义静态函数
    @staticmethod
    def staticMethod():
        print("this is a static method")

demo = Demo()
demo.getInfo();
Demo.staticMethod();
#使用id函数查看变量的唯一值
print(id(demo))
print(id(demo.address))
