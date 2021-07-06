from selenium import webdriver
import time
import urllib.request

driver = webdriver.Chrome("c:/driver/chromedriver.exe")

driver.get("https://www.naver.com/")
time.sleep(3)
driver.implicitly_wait(2)

# 검색창 찾기
tag = driver.find_element_by_name("query")

# 검색창에 글 입력
tag.send_keys("고양이")

# 검색버튼 누르는건데 나는 왜 실행이 안될까~??
# tag.send_keys(Keys.RETURN)

# 입력된 데이터 검색하게 그냥 해버리기.
tag.submit()
time.sleep(3)
driver.implicitly_wait(2)

# 이미지 탭 클릭
image = driver.find_element_by_link_text('이미지')
image.click()
time.sleep(3)
driver.implicitly_wait(2)


'''
반복문 시작
'''

# 첫번째 고양이 사진 클릭
images = driver.find_elements_by_css_selector("._image._listImage")
time.sleep(3)
driver.implicitly_wait(2)
count = 1
for image in images:
    image.click()
    print(image)
    print("------------------------------------------------------")

    # 클릭된 큰 고양이 사진 url 출력
    # print(driver.find_element_by_css_selector("._image").get_attribute("src"))
    # imgUrl = driver.find_element_by_css_selector("._image").get_attribute("src")
    imgUrl = image.get_attribute("src")
    
    # url 사진을 다운받자
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
    time.sleep(3)

    # 사진을 하나씩 세자
    count = count + 1