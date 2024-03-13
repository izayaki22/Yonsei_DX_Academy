# 문제 2번
# BeautifulSoup을 활용해 오늘의 인기 베스트에 올라온 세 작품을 크롤링하는 프로그램을 작성하세요.
# 작품의 제목과 별점을 모아 딕셔너리로 만들고 출력하세요.
# 예시 -> {'아무도 모르는 마녀': '9.28', '이래봬도2학년': '9.43', '견생&묘생': '7.60'}
# 네이버 웹툰의 베스트 도전 링크(https://comic.naver.com/genre/bestChallenge)


import requests
from bs4 import BeautifulSoup



# 1.페이지 정보 얻기
page = requests.get('https://comic.naver.com/genre/bestChallenge')

# 2.BeautifulSoup 로 파싱
soup = bs(page.text, 'lxml')

# 3.데이터 추출
# 3-1.오늘의 인기 베스트 데이터 추출
title_li = soup.find_all('div',class_='mainTodayImg')
grade_li = soup.find_all('dl',class_='mainTodayGrade')

# 3-2.제목과 별점 수집
subtlt=[]
grade=[]
result = {}  # 결과값을 저장
for temp in title_li:
    subtlt.append(temp.find('img')['title'])

for temp in grade_li:
    grade.append(temp.find('strong').text)

for temp in range(len(subtlt)):
    result[subtlt[temp]]=grade[temp]

print(result)

# 확인
