# spider——爬虫基础

```
baike_spider.py
```
用于爬取百度百科中的中外双语名词：中文通过定位head获取，外文通过定位百科中的['外文名', '英文名', '外文名称']等获取，也可修改为任意字符以定位其他元素。

```
financial_report_spider.py
```
用于爬取东方财富网的研报,保存PDF到本地：基于webdriver，模拟人工操作网页的行为，不易被反爬虫。

```
medical_corpus_spider.py
```
用于爬取医学NER名词的中英词对。
