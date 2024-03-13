import pandas as pd
from bs4 import BeautifulSoup as bs
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)

driver.maximize_window()

driver.get('https://www.youtube.com/@ysuniversity')
time.sleep(3)

#for temp in range(5):
#    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
#    time.sleep(1)

html = driver.page_source
soup = bs(html, 'lxml')

#result = soup.find_all('yt-formatted-string',id='video-title')

result = soup.find_all('h3')

youtube_dict={}

for temp in result:
    try:
        labeling= temp.find('a')['aria-label']
        for title_index in range(len(labeling)):
            if(labeling[title_index]=='게' and labeling[title_index+1]=='시' and labeling[title_index+2]=='자'):
                break
        for hits_index in range(len(labeling)):
            if(labeling[hits_index]=='조' and labeling[hits_index+1]=='회' and labeling[hits_index+2]=='수'):
                break

        youtube_dict[labeling[:title_index-1]] = labeling[hits_index+4:]
    except:
        pass

title_hits = pd.DataFrame.from_dict(youtube_dict, orient='index')
title_hits.columns=['조회수']
title_hits.index.name='연세대학교 유튜브 제목'
print(title_hits)