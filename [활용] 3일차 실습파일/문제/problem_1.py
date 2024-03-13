# 문제 1번
# BeautifulSoup을 활용해 네이버 웹툰의 제목을 크롤링하는 프로그램을 작성하세요.
# 요일별로 가장 높은 별점을 가진 웹툰을 크롤링하여 리스트로 만드세요.
# 네이버 웹툰 링크(https://comic.naver.com/webtoon/weekday?order=StarScore)


import requests
from bs4 import BeautifulSoup as bs



# 1.페이지 정보 얻기
page = requests.get("https://comic.naver.com/webtoon/weekday?order=StarScore")

# 2.BeautifulSoup 로 파싱
soup = bs(page.text, "html.parser")

# 3.데이터 추출
# 3-1.요일별 데이터 추출
data = soup.find_all('a',class_='title')

# 3-2.각 요일별로 가장 높은 별점을 가진 1개의 title 속성값을 추출
result = []  # 결과값을 저장
for temp in data:
    if("'1')" in temp['onclick']):
        result.append(temp['title'])
# 확인
print(result)
