from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from multiprocessing import Process

driver = webdriver.PhantomJS("D:\\phantomjs\\bin\\phantomjs.exe")
driver.get("http://fund.eastmoney.com/fund.html")
getPage_text = driver.find_element_by_id("pager").find_element_by_xpath("span[@class='nv']").text
allpage = ''.join(filter(str.isdigit, getPage_text))  # 得到一共多少页
# for
# 得到点击的span
def getData(myrange):
    for x in myrange:
        tonum = driver.find_element_by_id("tonum") #得到tonum文本框
        jumpbtn = driver.find_element_by_id("btn_jump") #跳转到按钮
        tonum.clear()
        tonum.send_keys(str(x))
        jumpbtn.click()
        WebDriverWait(driver, 20).until(lambda driver:driver.find_element_by_id("pager").find_element_by_xpath("span[@value={0} and @class!='end page']".format(x)) \
                                        .get_attribute("class").find("at") != -1)
        with open("../htmls/{0}.txt".format(x),'wb') as f:
            f.write(driver.find_element_by_id("tableDiv").get_attribute("innerHTML").encode('utf-8'))
            f.close()


r=range(1,int(allpage)+1)
step=10
range_list=[ r[x:x+step] for x in range(0,len(r),step)]# 把页码分段
processList=[]
if __name__ == '__main__':
    for r in range_list:
        p=Process(target=getData,args=(r,))
        processList.append(p)

    for p in processList:
        p.start()

