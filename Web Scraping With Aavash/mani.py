from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located




while True:

    video= input('Enter the songs name : ')

    vid = video.lower()
    if vid == 'pause':
        driver.getElementById("Video ID").play()

    if vid == 'play':
        driver.getElementById("Video ID").pause()

    if vid == 'stop':
        driver.close()


    # Navigate to url with video being appended to search_query
    
    else:
        driver.get('https://youtube.com/results?search_query={0}'.format(str(video)))

        # play the video
        wait.until(visible((By.ID, "video-title")))
        driver.find_element_by_id("video-title").click()