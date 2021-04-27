from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import time
from fake_useragent import UserAgent

base_url = "https://baike.baidu.com"
his = ["/item/%E9%A9%AC%E6%96%B9%E7%BB%BC%E5%90%88%E5%BE%81"]
# 根据自己的浏览器环境配置
# headers = {
#
# }
def spider():
    for i in range(1000):
        if base_url in his[-1]:
            url = his[-1]
        else:
            url = base_url + his[-1]

        html = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        info = {k.text.strip().replace('\xa0',''): v.text.strip().replace('\xa0','') for k, v in zip(soup.find_all('dt', {'class': ['basicInfo-item', 'name']}),
                                               soup.find_all('dd', {'class': ['basicInfo-item', 'value']}))}

        for key in info:
            if key in ['外文名', '英文名', '外文名称']:
                ename = info[key]
                print(i, soup.find('h1').get_text(), '', ename)


                f = open('name.txt', 'a', encoding='utf-8')

                f.write(soup.find('h1').get_text() + '$' +  ename)
                f.write('\n')
                # time.sleep(3)

        sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
        

        if len(sub_urls) != 0:
            his.append(random.sample(sub_urls, 1)[0]['href'])
        else:
            his.pop()
    return

if __name__=='__main__':
    while True:
        spider()
