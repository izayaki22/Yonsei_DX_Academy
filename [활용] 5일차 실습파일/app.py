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
from bs4 import BeautifulSoup as bs
import os
import sys

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

#region <1번> api서버구축
@app.route('/')
def index():
    return 'Hello, World!'
#endregion


#region <2번> 상품 최저가 검색
# naver api
client_id = "10czcu2mvdI2l632abVX"
client_secret = "7S5bFa76Be"

@app.route('/price/<keyword>')
def get_price(keyword):
    pencText = urllib.parse.quote(keyword)
    purl = "https://openapi.naver.com/v1/search/shop?query=" + pencText +'&sort=asc'
    prequest = urllib.request.Request(purl)
    prequest.add_header("X-Naver-Client-Id", client_id)
    prequest.add_header("X-Naver-Client-Secret", client_secret)
    presponse = urllib.request.urlopen(prequest)
    prescode = presponse.getcode()
    if (prescode == 200):
        presponse_body = presponse.read()
        presult = presponse_body.decode('UTF-8')
    else:
        presult = "Error Code:" + prescode
    pdata = json.loads(presult)
    return pdata['items'][0]['lprice']
#endregion


#region <3번> 책 정보 검색
@app.route('/book/<keyword>')
def get_book(keyword):
    book_dic={}

    client_id = "10czcu2mvdI2l632abVX"
    client_secret = "7S5bFa76Be"

    bencText = urllib.parse.quote(keyword)
    burl = "https://openapi.naver.com/v1/search/book?query=" + bencText
    brequest = urllib.request.Request(burl)
    brequest.add_header("X-Naver-Client-Id", client_id)
    brequest.add_header("X-Naver-Client-Secret", client_secret)
    bresponse = urllib.request.urlopen(brequest)
    brescode = bresponse.getcode()
    if (brescode == 200):
        bresponse_body = bresponse.read()
        bresult = bresponse_body.decode('UTF-8')
    else:
        bresult = "Error Code:" + brescode
    bdata = json.loads(bresult)
    book_dic['저자']=bdata['items'][0]['author']
    book_dic['발행연도']=bdata['items'][0]['pubdate']
        
    link = bdata['items'][0]['link']
    html = requests.get(link)
    soup = bs(html.text, 'html.parser')
    res = soup.find_all('div',class_="bookReview_book_review__lo_X6")
    for temp in res:
        book_dic['평점'] = temp.text[temp.text.index('평')+2:]
    return book_dic
#endregion


#region <4번> 공공데이터 사이트를 이용한 현재 날씨정보 리턴
@app.route('/weather')
def get_weather():
    url = 'http://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation'
    params = {'serviceKey': 'BMMurix5+MdNRWvky8MX1/WY7/G6Tzvgt9v2gQtpjiiFP8AuYVEZ6tb5V+eK5925HzUqk8BnuB9UXCev1pydUg==', 'pageNo': '1', 'numOfRows': '10', 'dataType': 'JSON', 'stnId': '108'}
    response = requests.get(url, params=params)
    result = json.loads(response.text)
    text = result['response']['body']['items']['item'][0]['wfSv1']
    for today in range(len(text)):
        if text[today]=='○':
            break
    for tmrw in range(len(text)):
        if text[tmrw]=='○'and text[tmrw+2]=='(' and text[tmrw+3]=='내':
            break 
    return text[today+7:tmrw]
#endregion


if __name__ == '__main__':
    app.run(debug=True)
