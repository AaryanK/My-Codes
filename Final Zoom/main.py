import os
import webbrowser
import requests
import webbrowser
import json
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


try:
    import PySimpleGUI
    from selenium import webdriver 
    import browsercookie
except:
    os.startfile("engine/installer.bat")

def authorize():
    driver = webdriver.Chrome()
    driver.get("https://us04web.zoom.us/signin")
    try:
        element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "meetings"))
    )
    finally:

        cookies = driver.get_cookies()
        pickle.dump(cookies,open("userdata/cookie.pkl","wb"))
        driver.quit()


def browser(cookie): 
    import time
    chrome_options = webdriver.ChromeOptions()
    prefs =  {
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
    }
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    cookies = pickle.load(open(cookie,"rb"))
    driver.get("https://us04web.zoom.us")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://us04web.zoom.us/j/8840743766?pwd=Q2Y3dmJMblo1bldkMXV0V3BtcUEvQT09#success")
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.LINK_TEXT, "Download Now")))

    driver.find_element_by_link_text("Download Now").click()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    driver.find_element_by_link_text("Join from Your Browser").click()

    time.sleep(15)
    element = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div[3]/div/button")))
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div[3]/div/button").click()

    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/footer/div/div[2]/button[3]/div/div")))
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/footer/div/div[2]/button[3]/div/div").click() 
    
    element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[4]/textarea")))
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[4]/textarea").send_keys("Good Morning")
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/div[4]/textarea").send_keys(Keys.RETURN)

    
    WebDriverWait(driver,timeout=40*60).until(EC.presence_of_element_located(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/h4"))


browser("userdata/cookie.pkl")