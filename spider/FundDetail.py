from selenium.webdriver.support.ui import WebDriverWait
from bs4 import  BeautifulSoup
from selenium import webdriver
from threading import Thread,Lock
import os
import csv
#初始化
def initSpider():
    driver = webdriver.PhantomJS()
    driver.get("http://fund.eastmoney.com/f10/jjjz_001112.html")  #基金详细页地址
    #找到下一页这个按钮 ，就可以得到他上面一个label，就是总页数
    getPage_text=driver.find_element_by_id("pagebar").find_element_by_xpath("div[@class='pagebtns']/label[text()='下一页']/preceding-sibling::label[1]").get_attribute("innerHTML")
    allpage = int(''.join(filter(str.isdigit, getPage_text)))  # 得到一共多少页
    return (driver,allpage)

def getData(myrange,driver,lock):
    for x in myrange:
        lock.acquire()
        if x==1: #第一页不需要处理 直接保存即可
            pass
        else:
            tonum =driver.find_element_by_id("pagebar").find_element_by_xpath("div[@class='pagebtns']/input[@class='pnum']")  # 得到 页码文本框
            jumpbtn = driver.find_element_by_id("pagebar").find_element_by_xpath("div[@class='pagebtns']/input[@class='pgo']")  # 跳转到按钮
            tonum.clear()
            tonum.send_keys(str(x))
            jumpbtn.click()
            WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("pagebar").find_element_by_xpath(
                "div[@class='pagebtns']/label[@value={0} and @class='cur']".format(x))!=None)
        with open("./htmls/details/{0}.txt".format(x), 'wb') as f:
            f.write(driver.find_element_by_id("jztable").get_attribute("innerHTML").encode('utf-8'))
            f.close()
            lock.release()

def beginSpider(): # 开始抓取 所有页面 保存到文件里
    (driver, allpage)=initSpider() # 注意这里的 代码写法
    lock =Lock()  # 创建锁
    r = range(1, int(allpage) + 1)
    step = 10
    range_list = [r[x:x + step] for x in range(0, len(r), step)]  # 把页码分段
    threadList=[]
    for r in range_list:
        t = Thread(target=getData, args=(r,driver,lock))
        threadList.append(t)
        t.start()
    for t in threadList:
        t.join() # 这一步是需要的，等待进程全部执行完成
    print("抓取完成")

# 使用beautiful soup 解析内容，大家也可以直接使用selenium,请随意
def getFundData(html):
    soup = BeautifulSoup(html, "html.parser")

    rows=soup.find("table").tbody.find_all("tr")
    result=[]
    for row in rows:
        tds=row.find_all('td')
        result.append({"fcode": '001112'
                       ,"fdate": tds[0].get_text()
                      , "NAV": tds[1].get_text()
                      , "ACCNAV": tds[2].get_text()
                      , "DGR": tds[3].get_text()
                      , "pstate":tds[4].get_text()
                      , "rstate": tds[5].get_text()
                      }
                  )
    return  result

#把抓取到的内容解析并写入csv文件
def writeToCSV():
    datadir = "./htmls/details"
    allpath = os.listdir(datadir)
    allresult=[]
    for p in allpath:
        if os.path.isfile(os.path.join(datadir, p)):
            with open(os.path.join(datadir, p), "rb") as f:
                fileCnt=f.read().decode('utf-8')
                f.close()
                allresult=allresult+getFundData(fileCnt)  #list合并 直接可用+   如list=list1+list2

    with open("./csvfiles/001112.csv",'w',encoding="utf-8",newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['fcode', 'fdate', 'NAV', "ACCNAV", 'DGR', 'pstate',"rstate"])
        for r in allresult:
            writer.writerow([r["fcode"],r["fdate"],r["NAV"],r["ACCNAV"],r["DGR"],r["pstate"],r["rstate"]])
        f.close()

