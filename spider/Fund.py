#基金抓取
from urllib import request
import chardet
from bs4 import  BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing.managers import BaseManager
from multiprocessing import Process
from selenium import webdriver
#------------------------下面是普通抓取html的程序
page1_url="http://fund.eastmoney.com/fund.html"
page2_url="http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=2,200&dt=1505405262745&atfc=&onlySale=0"

def getHtml(pageUrl):
    response =request.urlopen(pageUrl)
    raw_html=response.read()
    getEncoding=chardet.detect(raw_html)['encoding']
    return raw_html.decode(getEncoding)
def getPage(html):
    soup = BeautifulSoup(html, "html.parser")
    pageHtml=soup.find("div",id="pager").find("span","nv").get_text()
    return ''.join(filter(str.isdigit, pageHtml))


#--------------------------下面是利用selenium 抓取的程序员

bm = BaseManager(address=('', 8084), authkey=b'12345')
driver=None
allpage=0
def initSpider():
    driver = webdriver.PhantomJS()
    driver.get("http://fund.eastmoney.com/fund.html")
    getPage_text = driver.find_element_by_id("pager").find_element_by_xpath("span[@class='nv']").text
    allpage = int(''.join(filter(str.isdigit, getPage_text)))  # 得到一共多少页
def getData(myrange):
    for x in myrange:
        tonum = driver.find_element_by_id("tonum")  # 得到tonum文本框
        jumpbtn = driver.find_element_by_id("btn_jump")  # 跳转到按钮
        tonum.clear()
        tonum.send_keys(str(x))
        jumpbtn.click()
        WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("pager").find_element_by_xpath(
            "span[@value={0} and @class!='end page']".format(x)) \
                                        .get_attribute("class").find("at") != -1)
        with open("./htmls/{0}.txt".format(x), 'wb') as f:
            f.write(driver.find_element_by_id("tableDiv").get_attribute("innerHTML").encode('utf-8'))
            f.close()

def beginSpider(): #开始抓取 所有页面 保存到文件里
    if(driver==None):
        print("请先初始化,执行initSpider函数")
        exit()
    r = range(1, int(allpage) + 1)
    step = 10
    range_list = [r[x:x + step] for x in range(0, len(r), step)]  # 把页码分段
    processList = []
    for r in range_list:
        p = Process(target=getData, args=(r,))
        processList.append(p)
        p.start()
    for p in processList:
        p.join() #这一步是需要的，等待进程全部执行完成

#保存到数据库中
from sqlalchemy import create_engine,desc,text
from config.config import dbconfig
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from model.Fund import  Myfund
engine = create_engine(dbconfig,echo=True)

def getText(element):
    if element!=None:
        txt=element.get_text()
        if str(txt).strip()=="---":
            txt="0"
        return txt
    return ""

def getFundData(html): #解析基金数据
    soup = BeautifulSoup(html, "html.parser")
    fCodes = soup.find("table", id="oTable").tbody.find_all("td", "bzdm")  # 基金编码集合
    fDate=soup.find("table", id="oTable").thead.find("td",colspan='2').get_text() #基金日期

    result=[]
    for fCode in fCodes:
        # print(fCode.parent.find("td","rzzz"))
        # break
        print(fCode)
        result.append({"fcode":fCode.get_text()
                          ,"fname":fCode.next_sibling.find("a").get_text()
                          ,"NAV":getText(fCode.next_sibling.next_sibling)
                          ,"ACCNAV":getText(fCode.next_sibling.next_sibling.next_sibling)
                          ,"DGV":fCode.parent.find("td","rzzz").get_text()  #日增长值，取fcode所在的父元素(tr)，然后find
                          ,"DGR":fCode.parent.find("td","rzzl").get_text() #日增长率
                          ,"fee":getText(fCode.parent.find("div","rate_f")) #费率,注意这里不要定位到A元素,有的基金没有这个div，所以要做判断
                          ,"updatetime":datetime.now().isoformat(sep=' ',timespec="seconds")
                          ,"fdate":fDate}
                      )
    return result

def saveToDB():
    datadir = "./htmls"
    allpath = os.listdir(datadir)
    mysession = sessionmaker(engine)()
    dataList=[]
    for p in allpath:
        if os.path.isfile(os.path.join(datadir, p)):
            print(p)
            with open(os.path.join(datadir, p), "rb") as f:
                fileCnt=f.read().decode('utf-8')
                f.close()
            resultSet=getFundData(fileCnt)
            for result in resultSet:
                myfund=Myfund(**result)
                dataList.append(myfund)

    mysession.add_all(dataList) #批量新增
    mysession.commit()
    mysession.close()





