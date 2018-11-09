# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)


def run():
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_argument('user-agent=%s' % user_agent)
    # option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=option)

    with open('keywords.txt', encoding='utf-8', mode='r') as f:
        keywords = f.readlines()
    f.close()
    copy_keywords = [x for x in keywords]
    # 枚举实时调用迭代对象,仍是按索引响应更改,要复制一个出来
    for i, keyword in enumerate(copy_keywords):
        time.sleep(1)
        driver.get(
            'https://www.baidu.com/s?wd={}&rsv_spt=1&rsv_iqid=0xe6f606930001524e&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&oq=%25E5%2585%2583%25E5%25B0%258A&rsv_t=ce4478l3gG9Hm0LrQ0p%2F%2FgGyyjfpRezBg4K5wYrtCd3JQHDgg79qOr8LU4I3KG9EDbXi&rsv_pq=aec5c8f70000f057&prefixsug=%25E5%2585%2583%25E5%25B0%258A&rsp=0'.format(
                keyword.strip()))
        # 等待到底部帮助加载完成
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//div[@class="foot-inner"]'))
        try:
            WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath('//div[@class="tip_head"]'))
            keywords.remove(keyword)
            with open('keywords.txt', encoding='utf-8', mode='w') as f_new:
                f_new.writelines(keywords)
            f_new.close()
            print('没有找到与"' + keyword.strip() + '"相关的网页')
            continue
        except Exception :
            pass

        try:
            count = str(driver.find_element_by_xpath(
                '//div[@class="c-span21 c-span-last"]//p//b').text)
            count = count.lstrip('找到相关结果数约').rstrip('个').replace(',', '')
            print(keyword.strip(), ' ', count)
            with open('result.txt', encoding='utf-8', mode='a') as f_out:
                f_out.write(keyword.strip() + ' ' + count + '\n')
            f_out.close()
            keywords.remove(keyword)
            with open('keywords.txt', encoding='utf-8', mode='w') as f_new:
                f_new.writelines(keywords)
            continue
        except Exception :
            pass
        try:
            count = str(driver.find_element_by_xpath(
                '//div[@class="op_site_domain_right c-span24 c-span-last"]//p//span//b').text)
            count = count.replace(',', '')
            print(keyword.strip(), count)
            with open('result.txt', encoding='utf-8', mode='a') as f_out:
                f_out.write(keyword.strip() + ' ' + count + '\n')
            f_out.close()
            keywords.remove(keyword)
            with open('keywords.txt', encoding='utf-8', mode='w') as f_new:
                f_new.writelines(keywords)
            continue
        except Exception :
            pass


if __name__ == '__main__':
    run()
