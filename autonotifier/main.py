from selenium import webdriver
import time
from passwords import strong
# driver = webdriver.Chrome("pathtochromedriver.exe") for windows
driver = webdriver.Chrome()

driver.get("https://instagram.com")

with open("creds.py","r") as file:
    password = file.read()
    file.close()
time.sleep(3)

name = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
name.send_keys("dragonzpyder@gmail.com")
passwords = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
passwords.send_keys(password)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()

time.sleep(5)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

driver.get("https://www.instagram.com/accounts/password/change/")
time.sleep(3)
op = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[1]/div/input")
op.send_keys(password)

pas = strong(12)
np1 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[2]/div/input")
np1.send_keys(pas)
np2 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[3]/div/input")
np2.send_keys(pas)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/form/div[4]/div/div").click()

with open("creds.py",'w') as file:
    file.write(pas)
    file.close()

driver.close()

print("Password changed")
