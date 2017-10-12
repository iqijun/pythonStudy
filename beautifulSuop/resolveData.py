'''
解析抓取到的页面，在页面中读取，基金代码、名称、单位净值、累计净值等
'''

from bs4 import BeautifulSoup


with open("./grabResult/pageHtml.txt","rb") as f:
    html = f.read()
    f.close()

soup = BeautifulSoup(html,"html.parser")

table = soup.find("table",id="oTable")
bzdms = table.find_all("td",class_="bzdm")

result = ()
for bzdm in bzdms:
    name = bzdm.next_sibling.find("a").get_text()
    dwjz = bzdm.next_sibling.next_sibling.get_text()
    ljjz = bzdm.next_sibling.next_sibling.get_text()
    result += ({"name":name,"bzdm":bzdm.get_text(),"dwjz":dwjz,"ljjz":ljjz},)
    # print(name)
    # print(bzdm.get_text())
print(result)