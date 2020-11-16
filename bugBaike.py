from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random
import time
from fake_useragent import UserAgent

base_url = "https://baike.baidu.com"
his = ["/item/%E9%A9%AC%E6%96%B9%E7%BB%BC%E5%90%88%E5%BE%81"]
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Host':'baike.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
ua = UserAgent().data_randomize
header = {
    'User-Agent':ua
}
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
