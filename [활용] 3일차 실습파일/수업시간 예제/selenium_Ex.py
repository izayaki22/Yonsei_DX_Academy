import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()

driver.get('https://www.youtube.com/results?search_query=연세대학교')
time.sleep(3)

#driver.find_element(By.ID,'search').send_keys('고려대학교')
driver.find_element(By.XPATH,'//*[@id="text"]').click()

for temp in range(5):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)