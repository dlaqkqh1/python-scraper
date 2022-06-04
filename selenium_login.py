from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("./chromedriver")

# 1. 네이버로 이동
browser.get("https://naver.com")

# 2. 로그인 버튼 클릭
browser.find_element(By.CLASS_NAME, "link_login").click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("id")
browser.find_element(By.ID, "pw").send_keys("pw")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

# time.sleep(3)

# # 5. id 새로 입력
# browser.find_element(By.CLASS_NAME, "id").clear()
# browser.find_element(By.CLASS_NAME, "id").send_keys("dlacksdn12")
# browser.find_element(By.CLASS_NAME, "id").send_keys("cksdn12?")

# 6. html 정보 출력
print(browser.page_source)

# 7. browser.quit()