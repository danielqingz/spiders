from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = 'https://www.letpub.com.cn/index.php?page=med_english&class_id='

def medSpider(j):
    for i in range(46):
        url = base_url + str(j)
        print(url)
        html = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        for k in soup.find('div', id='content').find_all('a'):
            name = k.text.strip()
            f = open('medicalName.txt', 'a', encoding='utf-8')
            f.write(name)
            f.write('\n')
        j += 1

if __name__=='__main__':
    j = 1
    medSpider(j)
