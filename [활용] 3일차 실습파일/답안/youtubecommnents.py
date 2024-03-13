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
from bs4 import BeautifulSoup


# 1.크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def get_comment(keyword, count):
    # 2.크롬 열기 및 주소입력
    driver.get('https://www.youtube.com/results?search_query=' + keyword)

    # 3.영상 선택
    driver.find_element(By.XPATH, '//*[@id="dismissible"]/ytd-thumbnail').click()

    # 4.필요한 댓글 확보
    while True:
        # 4-1.페이지 읽기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        time.sleep(1)

        # 4-2.댓글 구역 추출하기
        comments_sections = soup.find_all('ytd-comment-thread-renderer', class_='ytd-item-section-renderer')

        # 4-3. while문 멈출지 체크
        if len(comments_sections) < count:  # 수집하려는 개수보다 확보된 댓글이 많다면
            body = driver.find_element(By.CSS_SELECTOR, 'body')
            body.send_keys(Keys.PAGE_DOWN)
            body.send_keys(Keys.PAGE_DOWN)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        else:
            del comments_sections[count:]  # 추출된 잉여 댓글 삭제
            break

    # 5. 이름과 댓글 크롤링
    username = []
    usercomment = []
    for item in comments_sections:
        try:
            a = item.find('yt-formatted-string', id='text').get_text()
            b = item.find('yt-formatted-string', id='content-text').get_text()
        except:
            a = item.find('a', id='author-text').get_text().strip()
            b = item.find('yt-formatted-string', id='content-text').get_text()
        username.append(a)
        usercomment.append(b)

    # 확인
    for i, j in zip(username, usercomment):
        print(f'{i}: {j}')


# 실행
get_comment('Me at the zoo', 5)