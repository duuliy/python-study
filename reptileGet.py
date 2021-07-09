import requests        #导入requests包
url = 'https://www.baidu.com/'
strhtml = requests.get(url)        #Get方式获取网页数据
print(strhtml.text)