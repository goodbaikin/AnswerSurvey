from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--diable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get('https://portal.student.kit.ac.jp/ead/?c=class_evaluation_list')

#ログイン処理
if driver.current_url[:27] == 'https://auth.cis.kit.ac.jp/':
    id = os.getenv('id')
    password = os.getenv('password')
    driver.find_element_by_id('username').send_keys(id)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_tag_name('button').click()
    
    time.sleep(1)

buttons  = driver.find_elements_by_name('reply_btn')
for i in range(len(buttons)):
    driver.switch_to.window(driver.window_handles[0])
    buttons[i].click()
    driver.switch_to.window(driver.window_handles[1])
    
    #ラジオボタン選択
    radio_buttons = driver.find_elements_by_xpath("//input[@type='radio'][@value='4']")
    for j in range(len(radio_buttons)):
        radio_buttons[j].click()
    #送信
    driver.find_element_by_id('save_btn').click()
    Alert(driver).accept()

    print ("{}/{} completed".format(i+1,len(buttons)))
    driver.close()

print ("回答が終了しました")
