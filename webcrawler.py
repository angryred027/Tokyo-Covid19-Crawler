import os
import sys
import time
import pandas as pd
from selenium import webdriver
from lxml import etree

chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://stopcovid19.metro.tokyo.lg.jp/zh-tw")
# Wait the time to fresh
time.sleep(5)
selector = etree.HTML(driver.page_source)

total_people = selector.xpath('//*[@id="tab-0"]/div/div/div[1]/div/div/div[4]/ul/li/div/span[2]/strong/text()')
everyday_number = selector.xpath('//*[@id="tab-0"]/div/div/div[2]/div/div/div[1]/div/div/span/text()')
date_and_daynumber = selector.xpath('//*[@id="tab-0"]/div/div/div[2]/div/div/div[1]/div/div/small/text()')

coronalist = []
coronalist.append([total_people,everyday_number,date_and_daynumber])

driver.close()

co = pd.DataFrame(coronalist)
co.columns = ['Total number','Daily infection','Date(increase or decrease)']
co.to_csv('/Users/bomin/Desktop/covid19.csv',index = False,encoding='utf_8_sig')
coronalist

# 發送信件
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def main():
    sender = 'text email account'
    gmail_password = 'password'
    recipients = ['email here']
    
    # 建立郵件主題
    outer = MIMEMultipart()
    outer['Subject'] = '東京都內最新疫情'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # 檔案位置
    attachments = ['/Users/bomin/Desktop/covid19.csv']

    # 加入檔案到MAIL底下
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                print ('can read faile')
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # 寄送EMAIL
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


main()