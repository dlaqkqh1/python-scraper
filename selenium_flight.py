from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def element_waiter(browser, finder):
    try:
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located(finder))
        return browser.find_element(finder[0], finder[1])
    except Exception as e:
        print(e)
        browser.close()
        quit()

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

url  = "https://flight.naver.com"

browser.get(url)

# ----- 날짜 선택 -----
# 가는 날 선택 클릭
browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6").click()

# 이번달 7일 선택
element_waiter(browser, (By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody//*[contains(text(), '7')]")).click()

# 8일 선택 딜레이 해결을 위해 명시적으로 오는 날 클릭
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[1]/div/button[2]").click()

# 이번달 8일 선택
element_waiter(browser, (By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody//*[contains(text(), '8')]")).click()

# ----- 제주도 선택 -----
# 도착지 선택
element_waiter(browser, (By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]")).click()

# 제주 검색
element_waiter(browser, (By.CLASS_NAME, "autocomplete_input__1vVkF")).send_keys("제주")

# 제주 선택
element_waiter(browser, (By.CLASS_NAME, "autocomplete_search_item__2WRSw")).click()

# 항공권 검색 클릭
element_waiter(browser, (By.CLASS_NAME, "searchBox_search__2KFn3")).click()

try:
    elem = element_waiter(browser, (By.XPATH, "//*[@id='__next']/div/div[1]/div[6]/div/div[2]/div[2]/div"))
    print(elem.text)

except Exception as e:
    print(e)
    browser.quit()

exit_key = input()
browser.quit()
