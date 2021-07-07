from selenium import webdriver
from bs4 import BeautifulSoup
import time

# def crawtub():
driver = webdriver.Chrome("c:/driver/chromedriver.exe")

driver.get("https://youtube-rank.com/board/bbs/board.php?bo_table=youtube")
time.sleep(3)
driver.implicitly_wait(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

channel_list = soup.select('tbody > tr') 
for channel in channel_list:
    title = channel.select('h1 > a')[0].text.strip()
    category = channel.select('p.category')[0].text.strip()
    subscriber = channel.select('.subscriber_cnt')[0].text
    view = channel.select('.view_cnt')[0].text
    video = channel.select('.video_cnt')[0].text 
    print(title, category, subscriber, view, video)

# hungry = driver.find_element_by_link_text('음식/요리/레시피')
# hungry.click()
# print("---------1-----------")
# time.sleep(3)
# print(driver.window_handles)
# print("---------2-----------")




# channel_list = soup.select('tr')

