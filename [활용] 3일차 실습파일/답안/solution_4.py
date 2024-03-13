# BeautifulSoup과 selenium을 활용해 검색어와 개수를 입력하면 네이버 뉴스에서 뉴스기사 제목을 개수만큼 크롤링하는 프로그램을 작성하세요.
# 검색어와 개수를 파라미터로 사용하는 함수를 작성하세요.
# 해당 함수가 크롤링한 데이터를 리스트로 만들어 리턴하도록 하세요.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


# 1.크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 2.크롬 열기 및 주소입력
driver.get('https://www.naver.com/')

title_list = []
def search(keyword, count):
    # 3.검색어 입력 및 실행
    driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(keyword)
    driver.find_element(By.XPATH, '//*[@id="search_btn"]').click()

    # 4.뉴스 탭 이동
    driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[8]/a').click()

    # 5.기사 크롤링
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    try:
        # 검색 범위 제한
        group = soup.find('ul', class_='list_news')
        group2 = group.find_all('li', class_='bx')
        # 호출 개수에 맞춰 데이터 수 편집
        if len(group2) > count:
            del group2[count:]
    except:
        print('error')

    # title 추출하여 리스트에 담기
    for temp in group2:
        title_list.append(temp.find('a', class_='news_tit')['title'])


# 함수 호출
search('월드컵', 3)

# 확인
print(title_list)