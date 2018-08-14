from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time


def login_checkin(email):
    try:
        browser = webdriver.Chrome()
        browser.get('http://poro.ws/auth/login')
        email_element = browser.find_element_by_id('email')
        email_element.send_keys(email)
        time.sleep(1)
        password_element = browser.find_element_by_id('passwd')
        password_element.send_keys(email)
        time.sleep(1)
        password_element.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'checkin')))
        browser.find_element_by_id('checkin').click()
        connect_list = [elem.text for elem in browser.find_elements_by_css_selector('[class="h4 font-bold m-t block"]')]
        info_list = [elem.text for elem in browser.find_elements_by_tag_name('strong')]



    except Exception as e:
        print(e)
    finally:
        # browser.close()
        pass

    # nydjck04839@chacuo.net  584219
    # aymgzi63459@chacuo.net
    # xleiow26403@chacuo.net
    # 1070969926@qq.com 320266
    # bwkhfz83467@chacuo.net

def register():
    mobile_emulation = {
        "deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.delete_all_cookies()
    try:
        browser.get('http://24mail.chacuo.net')
        email_element = browser.find_element_by_id('converts')
        email = email_element.get_attribute('value') + '@chacuo.net'
        print(email)
        browser.execute_script('window.open()')
        browser.switch_to.window(browser.window_handles[1])
        browser.get('http://poro.ws/auth/register')
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'email')))
        time.sleep(1)
        browser.find_element_by_id('email').send_keys(email)
        browser.find_element_by_id('sendcode').click()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(5)
        browser.refresh()
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'convertd')))
        browser.find_element_by_id('convertd').click()
        code = browser.find_element_by_id('mailview_data').find_element_by_tag_name('b').text
        print(code)
        time.sleep(2)
        browser.switch_to.window(browser.window_handles[1])
        browser.find_element_by_id('verifycode').send_keys(code)
        browser.find_element_by_id('passwd').send_keys(email)
        browser.find_element_by_id('repasswd').send_keys(email)
        browser.find_element_by_id('code').send_keys(584219)
        browser.find_element_by_id('reg').click()
        print('register success with '+email)
    except Exception as e:
        print(e)
    finally:
        time.sleep(3000)
        browser.close()


if __name__ == '__main__':
    # emil = 'aymgzi63459@chacuo.net'
    # login_checkin(emil)
    register()
