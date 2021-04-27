import time, os, re
from selenium import webdriver
import pandas as pd
import urllib.request

driver=webdriver.Chrome()  # 选择Chrome打开网页

def bug():
    name = []
    report_url = []

    driver.get('http://data.eastmoney.com/report/stock.jshtml')  # 打开网页

    for i in range(1, 100):
        def get_name():
            for i in range(1, 50):
                data = driver.find_element_by_xpath("//*[@id='stock_table']/table/tbody/tr[{}]/td[5]/a".format(i))
                # 定位所需内容的Xpath
                temp = data.text  # 保留文字
                name.append(temp)
        time.sleep(2)
        def get_report_url():
            for i in range(1, 50):
                url = driver.find_element_by_xpath("//*[@id='stock_table']/table/tbody/tr[{}]/td[5]/a".format(i))
                report_url_temp = url.get_attribute("href")  # 返回所指定的属性
                report_url.append(report_url_temp)
        get_name()
        get_report_url()
        driver.find_element_by_link_text("下一页").click()  # 跳转下一页
    data_Frame = pd.DataFrame({"Name": name, "url": report_url})  # 存为DataFrame
    data_Frame.to_excel('Report_url.xlsx', index=False, encoding='utf-8')  # 写进Excel

def pdfDownload():
    data = pd.read_excel('Report_url.xlsx')  # 从Excel读网址
    n = list(data['Name'])
    m = list(data['url'])
    for name, url in zip(n, m):
        driver.get(url)
        pdf = driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[4]/div[1]/div[1]/div[1]/div/span[5]/a")
        pdf = pdf.get_attribute("href")
        urllib.request.urlretrieve(pdf, 'output/{}.pdf'.format(name))  # 存到本地pdf


if __name__ == '__main__':
    bug()
    pdfDownload()
