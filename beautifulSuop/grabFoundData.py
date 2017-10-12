'''
抓取天天基金网内容，并写入文件
'''

from urllib import  request

response = request.urlopen("http://fund.eastmoney.com/jzzzl.html#os_0;isall_0;ft_;pt_1");
html = response.read() #以字节形式读取
# pageHtml = html.decode("gb2312")

#直接使用字节写入html文件
# with open("./grabResult/pageHtml.html","wb") as f:
#     f.write(html)
#     f.close()

#写入txt文件时，需要先以gb2312解码,再用utf8编码
with open("./grabResult/pageHtml.txt","wb") as f:
    f.write(html.decode("gb2312").encode("utf8"))
    f.close()


