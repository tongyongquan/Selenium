import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time


def click_tvbgj():
    mobile_emulation = {
        "deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS \
            X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.delete_all_cookies()
    browser.get('http://www.tvbgj.com/')

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'playbtn')))
    video_elements = browser.find_elements_by_class_name('playbtn')
    # ran = random.randint(0, len(video_elements) - 1)
    time.sleep(3)
    # print(video_elements[ran])
    # video_elements[ran]
    video_elements[0].click()
    while(True):
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'playbtn')))
        time.sleep(30)
        video_elements = browser.find_elements_by_class_name('playbtn')
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        video_elements[0].click()


if __name__ == '__main__':
    click_tvbgj()
