# flask를 활용해 api 서버를 구축하세요.
# 127.0.0.1:5000/ 으로 접속시 Hello, World! 를 리턴하는 코드를 작성하세요.
#
# 2번
# 127.0.0.1:5000/price/상품명 으로 요청시 입력받은 값으로 상품을 검색하고 상품의 최저가를 리턴하는 코드를 작성하세요.
# 네이버 api를 사용하세요.
#
# 3번
# 127.0.0.1:5000/book/책이름 으로 요청시 입력받은 값으로 책을 검색하고, 검색된 첫 번째 책의 이름과 저자, 발행연도, 평점을 딕셔너리 형태로 리턴하는 코드를 작성하세요.
# 네이버 api를 사용하세요.
#
# 4번
# 127.0.0.1:5000/weather 으로 요청시 현재 날씨를 리턴하는 코드를 작성하세요.
# 현재 날씨는 공공데이터 사이트의 ‘기상청_동네예보 통보문 조회서비스’ 오픈 api를 사용해 데이터를 받아오세요.(https://www.data.go.kr/index.do)

from flask import Flask, render_template
import datetime
import requests
import urllib.request
import json
from bs4 import BeautifulSoup


app = Flask(__name__)

#region <1번> api서버구축
@app.route('/')
def index():
    return 'Hello, World!'
#endregion


#region <2번> 상품 최저가 검색
# naver api
client_id = ''
client_secret = ''

@app.route('/price/<keyword>')
def get_price(keyword):
    encText = urllib.parse.quote(keyword)
    url = 'https://openapi.naver.com/v1/search/shop.json?query=' + encText
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', client_id)
    request.add_header('X-Naver-Client-Secret', client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    return result['items'][0]['lprice']
#endregion


#region <3번> 책 정보 검색
@app.route('/book/<keyword>')
def get_book(keyword):
    encText = urllib.parse.quote(keyword)
    url = 'https://openapi.naver.com/v1/search/book.json?query=' + encText
    request = urllib.request.Request(url)
    request.add_header('X-Naver-Client-Id', client_id)
    request.add_header('X-Naver-Client-Secret', client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)

    page = requests.get(result['items'][0]['link'])
    soup = BeautifulSoup(page.text, 'html.parser')
    layout = soup.find('ul', class_='bookTitle_list_info__yXUyF')
    # 저자
    author = layout.find('li', class_='bookTitle_item_info__IMLyY bookTitle_type_full__CLdPf')
    author = author.find('span', class_='bookTitle_inner_content__REoK1')
    print(author.get_text())
    # 발행일
    pudate = layout.find_all('li', class_='bookTitle_item_info__IMLyY')[3]
    pudate = pudate.find('span', class_='bookTitle_inner_content__REoK1')
    print(pudate.get_text())
    # 평점
    rating = soup.find('div', class_='bookReview_book_review__lo_X6')
    rating = rating.find('span', class_='bookReview_bg_star__69wBu')
    print(rating.nextSibling)

    result_a= {'저자': author.get_text(), '발행일': pudate.get_text(), '평점': rating.nextSibling.get_text()}
    return str(result_a)
#endregion


#region <4번> 공공데이터 사이트를 이용한 현재 날씨정보 리턴
@app.route('/weather')
def get_weather():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
    now = datetime.datetime.now()
    params = {'serviceKey': '+w8BvF2LAH8MlpXmACysPh6lI+4lKOueMCzfy1xhC94WAVN7vIYUtq5LovzZQ+p7MRSNiUza/Pb7m0jP36eVfg==',
              'pageNo': '1',
              'numOfRows': '1000',
              'dataType': 'JSON',
              'base_date': datetime.date.today().strftime('%Y%m%d'),
              'base_time': str(now.hour)+str(now.minute),
              'nx': '37',
              'ny': '126'}

    response = requests.get(url, params=params)
    print(response.content)
    result = json.loads(response.text)
    sky = ''
    for item in result['response']['body']['items']['item']:
        if item['category'] == 'SKY':
            sky = item['fcstValue']

    txt = ''
    if sky == '1':
        txt = '맑음'
    elif sky == '3':
        txt = '구름많음'
    elif sky == '4':
        txt = '흐림'

    return txt
#endregion


if __name__ == '__main__':
    app.run(debug=True)
