# <문제 3번>
# BeautifulSoup과 selenium을 활용해 지역별 날씨를 입력하면 네이버 검색창에 지역별 날씨를 검색하고, 현재 기온을 출력하는 프로그램을 작성하세요.
# 검색할 검색어를 인수로 받는 함수를 작성하세요.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 1.크롬 웹드라이버 설치 및 설정
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 2.크롬 열기 및 주소입력
driver.get('https://www.naver.com/')

def search_weather(keyword):
    # 3.검색어 입력 및 실행
    driver.find_element(By.XPATH, '//*[@id="query"]').send_keys(keyword)
    driver.find_element(By.XPATH, '//*[@id="search_btn"]').click()

    # 4.현재 기온 추출 및 출력
    a = driver.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/strong').text

    # 확인
    return a

# 함수 호출
print(search_weather('판교동 날씨'))