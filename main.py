name = r'xi\'ngguishuia'; # 原样输出转义字符\
print(name);
mutiLin = """
I 
am 
xingguishuai
"""
print(mutiLin) # 多行输出
# 输出三遍name变量
print(name*3)

#输出字符串中指定位置的字符
print(name[1]);

#截取字符串(含头不含尾)
print(name[3:6]);
#截取0~2
print(name[:2]);
#截取第二个以后的字符
print(name[2:])
# 字符串长度
print(len(name))

dict={'a':1,'b':2,'c':3};
list =[x+"="+str(y) for x,y in dict.items()]
for item in list:
    print(item);

# 函数定义和调用
#设置参数的默认值
def myFunction(name="cruise",age=18):
    #因为数字和字符串不能直接相加，所以使用str函数将数字转为字符串
    print(name+":"+str(age))
#调用示例
#不输入参数，输出默认值
myFunction();
#如果省略前面的参数则后面的参数要指定参数名
myFunction(age=20);  #输出 cruise:20
#如果指定参数名，则参数位置可以交换
myFunction(age=21,name="tom") # 输出内容 tom:21