
try:
    f = open("classExample.py","r")
    f.read()
except BaseException:
  
    print("抛出异常了")
finally:
    print("必定执行")