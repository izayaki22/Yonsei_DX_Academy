import time

import pyperclip as pyperclip
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) , options=chrome_options)

driver.maximize_window()
keyword = '메타버스'
url = (f"https://www.youtube.com/results?search_query={keyword}")

driver.get(url)
time.sleep(2)

body = driver.find_element(By.TAG_NAME,"body")

scrollcount = 0
while scrollcount < 10:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    scrollcount += 1

result = driver.find_elements(By.ID,'dismissible')

print(len(result))
for temp in result:
    title = temp.find_element(By.ID,'video-title').get_attribute('title')
    try:
        content = temp.find_element(By.CLASS_NAME,'metadata-snippet-text')
        ccount = temp.find_element(By.CLASS_NAME,'inline-metadata-item')
        print(title)
        print(content.text)
        print(ccount.text)
        print('============================================')
    except:
        print('======' + title)

