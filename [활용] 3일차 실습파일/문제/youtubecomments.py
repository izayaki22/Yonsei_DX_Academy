# BeautifulSoup과 selenium을 활용해 유튜브의 댓글을 크롤링하는 프로그램을 작성하세요.
# 검색어와 댓글 개수를 인수로 받아 실행하는 함수를 작성하세요.
# 검색된 첫 번째 영상의 링크로 이동하는 코드를 작성하세요.
# 이동 후 인수로 입력한 개수만큼 유저 이름과 댓글 내용을 크롤링 하세요.
# 유저 이름과 댓글은 각각 리스트로 저장하세요.


import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs


# 1.크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()



driver.get('https://www.youtube.com/results?search_query='+'침착맨')

driver.find_element(By.XPATH,'//*[@id="dismissible"]').click()
time.sleep(2)

for temp in range(20):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)

html = driver.page_source
soup = bs(html,'lxml')
time.sleep(1)

comment_sections = soup.find_all('yt-comment-thread-renderer',class_='ytd-item-section-renderer')
print('코멘트:',comment_sections)

'''
def get_comment(keyword, count):
    # 2.크롬 열기 및 keyword 가 포함된 주소입력
    driver.

    # 3.영상 선택
    driver.

    # 4.페이지를 스크롤하여 필요한 댓글 확보
    while True:
        # 4-1.페이지 읽기
        html =
        soup =
        time.sleep(1)

        # 4-2.댓글 구역 추출하기
        comments_sections =



    # 5. 이름과 댓글 크롤링
    username = []
    usercomment = []
    for item in comments_sections:
        # 이름, 댓글 탐색해 리스트에 추가

    # 확인
    for i, j in zip(username, usercomment):
        print(f'{i}: {j}')


# 실행
get_comment('Me at the zoo', 5)
'''