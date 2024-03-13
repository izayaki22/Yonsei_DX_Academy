# BeautifulSoup과 selenium을 활용해 멜론의 TOP100에서 100개의 곡정보를 크롤링하는 프로그램을 작성하세요.
# 크롤링한 곡 제목과 아티스트 이름을 딕셔너리로 만드세요.
# {'제목1': '아티스트1', '제목2': '아티스트2'}


import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()


header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
link = 'https://www.melon.com/chart/'

driver.get(link)
html=driver.page_source

# 2.BeautifulSoup 로 파싱
soup = bs(html,'lxml')

# 3.데이터 추출
# 3-1.오늘의 인기 베스트 데이터 추출
for temp in range(10):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
title_list=[]
artist_list=[]

result = soup.find_all('div',class_='ellipsis')

for temp in result:
    if 'playSong' in temp.find('a')['href']:
        title_list.append(temp.text.strip())
    elif 'goArtistDetail' in temp.find('a')['href']:
        ln=int(len(temp.text)/2)
        artist_list.append(temp.text[:ln].strip())

# 3-2.제목과 아티스트 수집
result_dict = {} # 결과값 수집
for temp in range(len(title_list)):
    result_dict[title_list[temp]]=artist_list[temp]

# 확인
print(result_dict)
print(len(result_dict)) # 100
