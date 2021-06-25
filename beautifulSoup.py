import requests        #导入requests包
from bs4 import BeautifulSoup
import time
import re
# time.sleep(3) 每 3 秒钟抓取一次
url='http://www.cntour.cn/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
strhtml=requests.get(url,headers=headers)
# 构建自己的代理 IP 池 避免被封ip
# proxies={
#     "http":"http://10.10.1.10:3128",
#     "https":"http://10.10.1.10:1080",
# }
# strhtml=requests.get(url,proxies=proxies)
soup=BeautifulSoup(strhtml.text,'lxml')
# data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
for item in data:
    result={
        "title":item.get_text(),
        "link":item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
print(result)
# print(data)