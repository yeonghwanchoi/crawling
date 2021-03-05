from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import pandas as pd


def get_items(city_name,town_name):
    
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://www.opinet.co.kr")
    time.sleep(2)
    driver.get("https://www.opinet.co.kr/searRgSelect.do")

    sido_list_raw = driver.find_element_by_id("SIDO_NM0")
#         sido_name=[option.get_attribute('value') for option in sido_list_raw.find_elements_by_tag_name('option')]
#         sido_name.remove('')
    time.sleep(2)
    sido_list_raw.send_keys(city_name)

    gu_list_raw = driver.find_element_by_id("SIGUNGU_NM0")
#         gu_name=[option.get_attribute('value') for option in gu_list_raw.find_elements_by_tag_name('option')]
#         gu_name.remove("")
    time.sleep(2)
       
    gu_list_raw.send_keys(town_name)
    
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')    
        
    source = soup.find_all('tbody')[0]
        
    page = source.find_all('td','rlist')
    price= source.find_all('td','price')
    p=re.compile('[\d]+')
    price=p.findall(str(price))
    
    return pd.DataFrame({'brand':get_brand(page),'self':get_isself(page),'name':get_name(page),'gas_price':gas_price(price),'diesel_price':diesel_price(price)})