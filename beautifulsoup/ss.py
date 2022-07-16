import os
os.environ['DISPLAY'] = ':0'
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.youtube.com')