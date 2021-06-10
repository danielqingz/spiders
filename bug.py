# version 1.3 2021-06-07

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions

import time
import linecache
import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument('src')
parser.add_argument('tgt')
parser.add_argument('start_line', type=int)
parser.add_argument('total_line', type=int)

args = parser.parse_args()

T1 = time.time()

driver = webdriver.Chrome()
driver.get("https://www.deepl.com/zh/translator")

try:
    elem_src = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[5]/div[3]/div[1]/div[2]/div[1]/textarea[1]")

    bu1 = driver.find_element_by_xpath(
        "//body/div[2]/div[1]/div[5]/div[3]/div[3]/div[1]/div[2]/div[1]/button[1]").click()
    bu2 = driver.find_element_by_xpath(
        "//button[contains(text(),'俄语')]").click()
    textarea_tgt = driver.find_element_by_xpath(
        "//body[1]/div[2]/div[1]/div[5]/div[3]/div[3]/div[3]/div[1]/div[1]")
    wrong_case = 0
    if not args.start_line:
        args.start_line = 1
    
    i = args.start_line - 1
    
    while args.total_line is None or i < args.total_line:
        retry = False
        i += 1
        line = linecache.getline(args.src, i) # src文件路径
        if args.total_line is None and line == "":
            break
        if len(line) >= 2000:
            out = open(args.tgt, 'a', encoding='utf-8') # tgt文件路径
            out.write('\n')
            continue
        elem_src.send_keys(line)
        cur_value = ""
        sample_wrong_case = 0
        while cur_value == '' or len(cur_value) == 1:
            sample_wrong_case += 1
            time.sleep(3.5)
            cur_value = textarea_tgt.get_attribute('textContent').replace('\n', '').replace('\r', '')
            if sample_wrong_case == 5:
                retry = True
                break
        if retry:
            print('retry: ' + str(i), flush=True)
            i -= 1
        else:
            print(cur_value, i)
            outline = cur_value + '\n'
            out = open(args.tgt, 'a', encoding='utf-8') # tgt文件路径
            out.write(outline)
            out.close()
        elem_src.clear()
        
except KeyboardInterrupt:
    print('stop')

finally:
    driver.quit()
    print('finish')

T2 = time.time()

print('程序运行时间:%s秒' % (T2 - T1))
