
import requests        #导入requests包
from bs4 import BeautifulSoup  
# 这个方法只能爬静态网页  pass
# py用selenium

url = 'http://192.168.1.1/'
req = requests.get(url)       
html = req.text
bf = BeautifulSoup(html,"html.parser")
# texts = bf.find_all('input', id = 'lgPwd') 
texts = bf.find_all('div',id='Login') 
# texts = bf.find_all('span',class_='hardwareinfo') 
print(texts)



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# print(driver)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# print(elem)
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
