# BeautifulSoup과 selenium을 활용해 멜론의 TOP100에서 100개의 곡정보를 크롤링하는 프로그램을 작성하세요.
# 크롤링한 곡 제목과 아티스트 이름을 딕셔너리로 만드세요.
# {'제목1': '아티스트1', '제목2': '아티스트2'}


import requests
from bs4 import BeautifulSoup


# 1.페이지 정보 얻기
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
page = requests.get('https://www.melon.com/chart/', headers=header)

# 2.BeautifulSoup 로 파싱
soup = BeautifulSoup(page.text, 'html.parser')

# 3.데이터 추출
# 3-1.오늘의 인기 베스트 데이터 추출
li_1 = soup.find_all('tr', class_='lst50')
li_2 = soup.find_all('tr', class_='lst100')

# 3-2.제목과 아티스트 수집
result = {} # 결과값 수집
for temp in li_1:
    title = temp.find('div', class_='ellipsis rank01').get_text().strip()
    artist = temp.find('span', class_='checkEllipsis').get_text()
    result[title] = artist
for temp in li_2:
    title = temp.find('div', class_='ellipsis rank01').get_text().strip()
    artist = temp.find('span', class_='checkEllipsis').get_text()
    result[title] = artist

# 확인
print(result)
