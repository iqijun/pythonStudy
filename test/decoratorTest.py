# 装饰器

def Me(func):
    def showAll(*args):
        print("名字是shenyi")
        func(*args)
    return showAll

class Man:
    def __init__(self):
        self.sex = '男'
    @Me
    def showMan(self):
        print("年龄:19岁")
man=Man()
man.showMan()
print(man.sex)


#staticmethod、classmethod和property，作用分别是把类中定义的实例方法变成静态方法、类方法和类属性


class Man:
    def __init__(self):
        self.sex = '男'

    @property
    def mysex(self):
        return "我是"+self.sex

man=Man()
print(man.mysex)

