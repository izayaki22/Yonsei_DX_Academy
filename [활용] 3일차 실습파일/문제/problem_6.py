# BeautifulSoup과 selenium을 활용해 검색어를 입력하면 네이버 지식백과에서 검색 후, 요약된 내용과 제목를 크롤링하는 프로그램을 작성하세요.
# 크롤링한 링크와 제목, 요약을 각각 리스트로 저장하세요.


import requests
from bs4 import BeautifulSoup


# 1.requests를 이용해 페이지 정보 얻기
keyword = '호날두'
page = requests.get('https://terms.naver.com/search.naver?query='+keyword)

# 2.BeautifulSoup 로 파싱
soup = bs(page.text,'lxml')

# 3.데이터 추출
# 3-1.오늘의 인기 베스트 데이터 추출
li = soup.find_all('div',class_='info_area')

# 3-2.제목과 요약 수집
title_list = []
content_list = []
# for문을 사용해 데이터 수집
for temp in li:
        title_list.append(temp.find('strong').text)
        content_list.append(temp.find('p').text)
# 확인
for i,j in zip(title_list, content_list):
    print(f'{i}: {j}')
