'''
私有变量的使用 在变量名前面添加__
'''
#定义一个class

class Demo:
    #定义一个私有变量
    __sex = "男"
    #类似于构造函数
    def __init__(self):
        self.name = "cruise";
    #定义私有方法
    def __getInfo(self):
        print("name:"+self.name+";地址：")
    #定义静态函数
    @staticmethod
    def staticMethod():
        print("this is a static method")

# demo = Demo()
# #调用私有方法
# demo._Demo__getInfo();
# Demo.staticMethod();
# #使用id函数查看变量的唯一值
# print(id(demo))
# #调用私有属性
# print(demo._Demo__sex)
#
#
# print(__doc__)
# #入口方法 固定字符串 __main__
# print(__name__)
# #类的名称
# print(Demo.__name__)
# #类的属性，以字典形式显示
# print(Demo.__dict__)
# #对象的属性，只显示对象self属性中的属相（以字典方式展示）
# print(demo.__dict__)