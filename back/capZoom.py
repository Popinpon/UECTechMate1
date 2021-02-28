# -*- coding: utf-8 -*-
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import setting

repeatTime=5

options=Options()

if os.name == 'nt':
    print('on Windows')
elif os.name == 'posix':
    options.binary_location="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

userdata_dir = r'C:SelenUserData'
options.add_argument('--user-data-dir=' + userdata_dir)
driver = webdriver.Chrome(chrome_options=options,executable_path="./chromedriver_win32/chromedriver")
zoomURL="https://uec-tokyo.zoom.us/j/95142903465?pwd=NkIyRzVaZkxGYUNLV0lTOU5vNkFQdz09"
driver.get(zoomURL)
time.sleep(5)
element=driver.find_element_by_xpath('//*[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/a')
time.sleep(1)
element.click()

os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")


room_names=list(setting.YT_URL)
for count in range(repeatTime):
    for i,room in enumerate(room_names):
        time.sleep(1)
        driver.save_screenshot("../dist/static/img/"+room+str(count)+".png")
        time.sleep(5)
driver.quit()
