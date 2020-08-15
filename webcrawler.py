import os
import sys
import time
import csv
import pandas as pd
from selenium import webdriver
from lxml import etree


chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://stopcovid19.metro.tokyo.lg.jp/zh-tw")

# Wait the time to fresh
time.sleep(10)
selector = etree.HTML(driver.page_source)

total_people = selector.xpath('//*[@id="tab-0"]/div/div/div[1]/div/div/div[4]/ul/li/div/span[2]/strong/text()')
everyday_number = selector.xpath('normalize-space(//*[@id="tab-0"]/div/div/div[4]/div/div/div[1]/div/div/div/span/text())')
date_and_daynumber = selector.xpath('//*[@id="tab-0"]/div/div/div[2]/div/div/div[1]/div/div/small/text()')

coronalist = []
coronalist.append([total_people,everyday_number,date_and_daynumber])

driver.close()
print ('done!')

co = pd.DataFrame(coronalist)
co.columns = ['Total number','Daily infection','Date(increase or decrease)']
co.to_csv('/Users/bomin/Documents/tokyocovid19crawler/covid19.csv',index = False,encoding='utf_8_sig')
coronalist