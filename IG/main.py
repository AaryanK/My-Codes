from time import sleep
from selenium import webdriver
from sympy import Q

driver1 = webdriver.Chrome("chromedriver.exe")
# driver2 = webdriver.Chrome("chromedriver.exe")


def mail(driver1):
    mail = driver1.find_element_by_xpath("/html/body/section[1]/div[2]/div/div[2]/div/div/div[1]/input")
    return mail.get_attribute('value')

driver1.get("https://tempail.com/en/")
sleep(2)
error = True
while error:
    try:
        email = mail(driver1)
        error = False
        
    except:
        sleep(2)


