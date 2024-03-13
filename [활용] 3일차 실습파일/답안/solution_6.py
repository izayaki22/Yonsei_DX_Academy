# BeautifulSoup과 selenium을 활용해 검색어를 입력하면 네이버 지식백과에서 검색 후, 요약된 내용과 제목, 제목에 포함된 링크를 크롤링하는 프로그램을 작성하세요.
# 크롤링한 링크와 제목, 요약을 각각 리스트로 저장하세요.


import requests
from bs4 import BeautifulSoup


# 1.페이지 정보 얻기
keyword = '호날두'
page = requests.get(f'https://terms.naver.com/search.naver?query={keyword}&searchType=text&dicType=&subject=')

# 2.BeautifulSoup 로 파싱
soup = BeautifulSoup(page.text, 'html.parser')

# 3.데이터 추출
# 3-1.오늘의 인기 베스트 데이터 추출
li = soup.find_all('div', class_='info_area')

# 3-2.제목과 아티스트 수집
title_list = []
content_list = []
for temp in li:
    title = temp.find('strong', class_='title').get_text()
    content = temp.find('p', class_='desc').get_text()
    title_list.append(title)
    content_list.append(content)

# 확인
for i,j in zip(title_list, content_list):
    print(f'{i}: {j}')
