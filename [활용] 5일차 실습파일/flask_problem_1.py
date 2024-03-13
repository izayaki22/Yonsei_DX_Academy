# 1번
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

def index():

#endregion


#region <2번> 상품 최저가 검색
# naver api
client_id = ''
client_secret = ''


def get_price(keyword):

#endregion


#region <3번> 책 정보 검색

def get_book(keyword):

#endregion


#region <4번> 공공데이터 사이트를 이용한 현재 날씨정보 리턴

def get_weather():

#endregion


if __name__ == '__main__':
    app.run(debug=True)
