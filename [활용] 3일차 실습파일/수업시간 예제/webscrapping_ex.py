import requests
from bs4 import BeautifulSoup as bs

html = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
soup = bs(html.text, 'html.parser')

result = soup.find_all('div',class_='tit3')

for temp in result:
    print(temp.find('a')['title'])