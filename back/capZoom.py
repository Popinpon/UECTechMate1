# -*- coding: utf-8 -*-
import time,os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import setting
import requests
from PIL import Image
import json
import base64
from io import BytesIO
repeatTime=5

options=Options()

if os.name == 'nt':
    print('on Windows')
elif os.name == 'posix':
    options.binary_location="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

userdata_dir = r'C:SelenUserData'
options.add_argument('--user-data-dir=' + userdata_dir)
driver = webdriver.Chrome(chrome_options=options,executable_path="./chromedriver_win32/chromedriver")

driver.get("http://localhost:9999")

time.sleep(1)
passcode="0023269450"
meeting="941 1475 9766"
# time.sleep(5)

clearBtn='//*[@id="clear_all"]'
element=driver.find_element_by_xpath(clearBtn)
element.click()
time.sleep(0.5)
element=driver.find_element_by_xpath('//*[@id="display_name"]')
element.send_keys()
time.sleep(0.1)
element=driver.find_element_by_xpath('//*[@id="meeting_number"]')
element.send_keys(meeting)
element=driver.find_element_by_xpath('//*[@id="meeting_pwd"]')
time.sleep(1)
element.send_keys(passcode)
element=driver.find_element_by_xpath('//*[@id="join_meeting"]')
time.sleep(1)
element.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
room_names=list(setting.YT_URL)
for count in range(repeatTime):
    for i,room in enumerate(room_names):
        time.sleep(1)
    #    element=driver.find_element_by_xpath('//*[@id="wc-container-left"]/div[4]/div/div[2]/canvas')
        imgpath='../dist/static/img/'+room+str(count)+".png"
        png=driver.save_screenshot(imgpath)
        time.sleep(5)


        img = Image.open(imgpath)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_byte = buffered.getvalue()
        img_base64 = base64.b64encode(img_byte)

        img_str = img_base64.decode('utf-8')
        json_data = {
            "room_type": "A",
            "img": img_str
        }
        r = requests.post("http://localhost:5000/save_img",
                          json=json.dumps(json_data))
        print(r.json())
#time.sleep(5)
#driver.quit()
