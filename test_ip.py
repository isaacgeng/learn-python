# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 10:08:49 2017
To do list:

    2. add the sleep time after each inquiry to avoid blockness
@author: 耿浩
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from  selenium.common import exceptions
# 代理ip设置
## 配置代理ip,并测试代理ip
#options = webdriver.ChromeOptions()
#options.add_argument('--proxy-server=http://122.72.18.35:80')
#driver = webdriver.Chrome(chrome_options=options)
#driver.get('http://httpbin.org/ip')
#Proxy_text = driver.page_source
#driver.quit()
#
### get my ip address
#driver = webdriver.Chrome()
#driver.get('http://httpbin.org/ip')
#my_ip_text = driver.page_source
#driver.quit()
#
### 如果代理ip和我的ip不一样，那么可以开始爬取
#
#if Proxy_text != my_ip_text:
#    permission = True
#else :
#    print('Please Change the Proxy!')
#    permission = False
#    
#if permission == True:
#    company_list=["中泰证券"]
#    get_main_page("中泰证券")
#else :
#    driver.quit()
#    print('代理ip无效，已经退出')

# 爬取主体
## 1. 通过代理ip进入企查查主页
def get_main_page(Company_name):
    options = webdriver.ChromeOptions()
#    options.add_argument('--proxy-server=http://111.62.251.68:80')
#    options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU \
#    iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 \
#    (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"')
    options.add_argument(r'user-data-dir=C:\Users\耿浩\AppData\Local\Google\Chrome\User Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://www.qichacha.com/')
    #登陆
#    driver.find_element_by_xpath("/html/body/header/div/div[2]/a[2]").click()
#    time.sleep(2.9)
#    normal_login = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,\
#                                "//*[@id=\"normalLogin\"]")))
#    normal_login.click()
#    user_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,\
#                                  '//*[@id="user_login_normal"]/div[1]/input')))
#    time.sleep(2)
#    user_name.clear()
#    time.sleep(3)
#    user_name.send_keys("18253185659")
#    password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,\
#                                  '//*[@id="user_login_normal"]/div[1]/input')))
#    time.sleep(60)
    #等待搜索框加载完毕,休眠4秒
    time.sleep(4)
    # 找到搜索框
    try:
        search_box = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,\
                                  '//*[@id="searchkey"]')))
        #清除默认值
        search_box.clear()
        time.sleep(2)
        ## 2.定位到搜索框，键入所要搜索的 ‘变量’ 待定义, press enter 
        search_box.send_keys(Company_name)
        time.sleep(5)
        search_box.send_keys(Keys.ENTER)
        time.sleep(4.8)
        assert "小查还没找到数据" not in driver.page_source
        ## 3.找到第一个的网址，开始第二层
        try:
            first_item = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,\
                                  '//*[@id="searchlist"]/table/tbody/tr[1]/td[2]/a')))
            first_item.click()
            time.sleep(5)
        except:
            exceptions.NoSuchElementException
            print('第一个搜索项没找到')
#        else:
#            print('有啥错误没找到，反正第一个没搜索出来')
#            driver.close()
        ## 4.可能会出现没有打开新标签页的情况，没关系
        ## 将鼠标移到这一个标志的中央，再移动到最上方，点击
        try:
            driver.switch_to_window(driver.window_handles[-1])
            nianbao = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,\
                                  '企业年报')))
            nianbao.click()
            time.sleep(4)
            assert "咦，该企业还没有年报数据" not in driver.page_source
            driver.find_element_by_xpath("//*[@id=\"myTab\"]/li[2]/a").click()
            #下面爬取表格
        except:
            exceptions.NoSuchElementException
            print('没有年报这个按钮')
#        finally:
#            print('咦，有啥错误我没捕捉到啊')            
#            time.sleep(2)
        
    finally:
        df = pd.read_html(driver.page_source,match = '发起人',\
                              attrs={"class":"table table-bordered m_colorOdd"}\
                              ,header=0)[0]
        df["company_name"] = Company_name
        df.to_csv("C:\\Users\\耿浩\\Downloads\\Share_detail_2015\\%s.csv"%Company_name)
        print('hh')
        driver.close()
        
get_main_page('奇虎')

## 4.进入这一网址，等待加载，并且点击第三个标签‘企业年报’，
## 5.企业年报