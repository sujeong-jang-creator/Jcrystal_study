from selenium import webdriver
import time
import urllib.request

def crawcat():
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
    lst = []
    for image in images:
        image.click()
        print(image)
        print("------------------------------------------------------")

        # 클릭된 큰 고양이 사진 url 출력
        # print(driver.find_element_by_css_selector("._image").get_attribute("src"))
        # imgUrl = driver.find_element_by_css_selector("._image").get_attribute("src")
        imgUrl = image.get_attribute("src")
        lst.append(imgUrl)
        # url 사진을 다운받자
        # urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        time.sleep(3)

        # 사진을 하나씩 세자
        count = count + 1

    print(lst)
    return lst


# ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MjZfMTYz%2FMDAxNjI0NzE1ODQ3NjE1.OM0xi6eJ3aYoWk2wXA5zRwHgGeV8pH9IQ5LFYuH_-4Ig.P_4KS-sGBkhEgF9zjsy6jps47lqYEZztqnbeLCUSlTwg.JPEG.fjql004%2FDSC04394.JPG&type=a340', 
# 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MjVfNjgg%2FMDAxNjI0NjE1MTY3NTE1.ZAHTmN9XKVId8j4tulxCxuWRId1DTWknYHovHNBm-lMg.qko9j6AAg6O-ZJEbSVz_8K2ASd74dKKcCj6NiHm8KeUg.JPEG.western_animal%2F%25C0%25DA%25B9%25A6%25BD%25C3%25B1%25E2.jpg&type=a340', 
# 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA3MDNfODIg%2FMDAxNjI1MzE5NzEwMTE5.dRHMPvNNwkfXiCXbCdPvMI4qxCXtSoC5vsckbup1_MMg.W8YEPW9E3xFnuk36rwp5neKIU32sKNulr26Lts4B80og.JPEG.skdlzl8686%2FIMG_0414.JPG&type=a340', 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA3MDFfMTcz%2FMDAxNjI1MTE1MjEyNzIy.-ykqIsqE9v8IYgsA43xwOKTdwP6GpGaDD7mGMHr4o14g.S0p5z08Ks2GDjw9pbeYQttkEcqRNM8W4eUN_y7ZSA3Ag.JPEG.swfruitjuice%2FKakaoTalk_20210701_134947530_02.jpg&type=a340', 
# 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MTlfMTYz%2FMDAxNjI0MDI5NTY2MTg1.UoBmQAZO79kqwyYGUazp7-68O9NKK_T_MD8nPqXTdzwg.BR9bpnp-Q3F5mnmcCQPrQggBOUWlQY6Ltll8xbZsodog.JPEG.yjhaimi%2FScreenshot%25A3%25DF20210618%25A3%25AD233236%25A3%25DFSamsung_Internet.jpg&type=a340']