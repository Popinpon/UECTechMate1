# -*- coding: utf-8 -*-
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



options=Options()
if os.name == 'nt':
    print('on Windows')
elif os.name == 'posix':
    options.binary_location="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

userdata_dir = r'C:SelenUserData'
options.add_argument('--user-data-dir=' + userdata_dir)
driver = webdriver.Chrome(chrome_options=options,executable_path="./chromedriver_win32/chromedriver")

driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()
