# BeautifulSoup과 selenium을 활용해 검색어와 개수를 입력하면 네이버 뉴스에서 뉴스기사 제목을 개수만큼 크롤링하는 프로그램을 작성하세요.
# 검색어와 개수를 파라미터로 사용하는 함수를 작성하세요.
# 해당 함수가 크롤링한 데이터를 리스트로 만들어 리턴하도록 하세요.


import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# 1.크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()

# 2.크롬 열기 및 주소입력
driver.get('https://www.naver.com/')

# search 라는 이름의 함수를 만들고, keyword, count라는 이름의 매개변수를 등록
def search(keyword, count):
    title_list = []  # 결과값을 저장

    # 3.검색어 입력 및 실행
    driver.find_element(By.ID, 'query').send_keys(keyword)
    driver.find_element(By.ID, 'search_btn').click()
    time.sleep(2)

    # 4.뉴스 탭 이동
    driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/ul/li[8]').click()

    # 5.기사 크롤링
    html = driver.page_source
    soup = bs(html, 'lxml')

    try:
        result = soup.find_all('a', class_='news_tit')
    except:
        print('error')

    # title 추출하여 리스트에 담기
    cnt=0
    for tlt in result:
        if cnt<count:
            title_list.append(tlt['title'])
            cnt+=1
        else:
            break


    # 리턴
    return title_list


# 함수 호출 및 결과 확인
print(search('루시', 3))
