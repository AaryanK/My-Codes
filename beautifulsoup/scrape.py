from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://youtube.com")
a = driver.find_element_by_xpath('//*[@id="search"]').send_keys("stale")

