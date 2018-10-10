import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time


def login_check_in(email):
    vpn = {}
    mobile_emulation = {
        "deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS \
            X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.delete_all_cookies()
    try:
        browser.get('http://poro.ws/auth/login')
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'email')))
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

        vpn['email'] = email
        vpn['total'] = info_list[0]
        vpn['used'] = info_list[1]
        vpn['un_used'] = info_list[2]
        vpn['status'] = info_list[3]
        vpn['port'] = connect_list[0]
        vpn['password'] = connect_list[1]
        vpn['encryption'] = connect_list[2]
        vpn['last_login'] = connect_list[3]
        if '可以签到' in browser.find_element_by_class_name('col-xs-8').text[-19:]:
            vpn['last_check_in'] = datetime.datetime.now()
        else :
            vpn['last_check_in'] = datetime.datetime.strptime(browser.find_element_by_class_name('col-xs-8').text[-19:], '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print(e)
    finally:
        browser.close()
    return vpn



def register():
    mobile_emulation = {
        "deviceMetrics": {"width": 414, "height": 736, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS \
        X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.delete_all_cookies()
    try:
        browser.get('http://24mail.chacuo.net')
        email_element = browser.find_element_by_id('converts')
        email = email_element.get_attribute('value') + '@chacuo.net'
        print("[+] get email: " + email)
        browser.execute_script('window.open()')
        browser.switch_to.window(browser.window_handles[1])
        browser.get('http://poro.ws/auth/register')
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'email')))
        browser.find_element_by_id('email').send_keys(email)
        wait.until(EC.presence_of_element_located((By.ID, 'sendcode')))
        browser.find_element_by_xpath('//span[@class="input-group-btn"]/button').click()
        # browser.find_element_by_id('sendcode').click()
        time.sleep(1)
        browser.switch_to.window(browser.window_handles[0])
        print('[-] waiting email...')
        wait = WebDriverWait(browser, 300)
        wait.until(EC.presence_of_element_located((By.XPATH, '//tbody[@id="convertd"]/tr')))
        browser.find_element_by_id('convertd').click()
        time.sleep(3)
        code = [code.text for code in browser.find_elements_by_tag_name('b')]
        print('[+] get code: '+code[-2])
        browser.switch_to.window(browser.window_handles[1])
        browser.find_element_by_id('verifycode').send_keys(code[-2])
        browser.find_element_by_id('passwd').send_keys(email)
        time.sleep(1)
        browser.find_element_by_id('repasswd').send_keys(email)
        browser.find_element_by_id('code').send_keys(320266)
        browser.find_element_by_id('reg').click()
        print('[+] register success with ' + email)
    except Exception as e:
        print(e)
    finally:
        browser.close()


if __name__ == '__main__':
    # emil = 'xleiow26403@chacuo.net'
    # vpn = login_check_in(emil)
    # print(vpn)
     register()

# ssr 修改备注 replace:JnJlbWFya3M9Y0c5eWJ5NTNjLVdGamVpMHVlZUppT2F6bGVXYnZlZTZ2LWkzcncmZ3JvdXA9VUc5eWItV0ZqZWkwdWVlSmlB
# JnJlbWFya3M9NW9pUjU1cUVjM055UHo4Jmdyb3VwPTVvaVI1NXFFYzNOeVB6OA
# uerdfx49102@chacuo.net