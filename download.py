from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os

main_url = "https://www.naver.com/"
driver = webdriver.Chrome("C:\\driver\\chromedriver.exe")
driver.get(main_url)
print('1. naver 접속 완료')