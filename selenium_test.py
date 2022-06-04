from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome("./chromedriver")
browser.get("https://naver.com")

# elem = browser.find_element(By.CLASS_NAME, "link_login")    # CLASS_NAME 를 통해 엘레멘트 가져오기
# elem.click()                                                # 클릭 실행

elem = browser.find_element(By.ID, "query")                   # ID 를 통해 엘레멘트 가져오기
elem.send_keys("나도코딩")                                      # 엘레멘트에 값 넘기기
elem.send_keys(Keys.ENTER)                                    # 문자열 이외 값 Keys 를 통해 입력 가능

elem = browser.find_elements(By.TAG_NAME, "a")

for e in elem:
       print(e.get_attribute("href"))

browser.get("https://daum.net")

elem = browser.find_element(By.NAME, "q")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

browser.back()

elem = browser.find_element(By.NAME, "q")
elem.send_keys("나도코딩")
elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()


while True:
    pass