import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

url  = "https://flight.naver.com"

browser.get(url)

# 가는 날 선택 클릭
browser.find_element(By.CLASS_NAME, "tabContent_option__2y4c6").click()

time.sleep(0.3)

# 이번달 7일 선택
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody//*[contains(text(), '7')]").click()
time.sleep(0.3)
browser.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody//*[contains(text(), '8')]").click()
