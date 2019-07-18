# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.chrome.service as service
import csv

CHROME_DRIVER_PATH = '/Users/hd-imac/Downloads/chromedriver'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.zerogravity.booster&appid=4972385200317449506&appVersion=PRODUCTION&lastReportedRange=LAST_30_DAYS&errorType=ANR&installSource=INSTALLED_FROM_PLAY'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5115057263789938963#AndroidMetricsErrorsPlace:p=com.pixel.art.coloring.color.by.number&appid=4975206524895984119&lastReportedRange=LAST_30_DAYS&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5115057263789938963#AndroidMetricsErrorsPlace:p=com.bongolight.pixelcoloring&appid=4973594308926896530&lastReportedRange=LAST_30_DAYS&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.zerogravity.booster&appid=4972385200317449506&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.zerogravity.booster&appid=4972385200317449506&lastReportedRange=LAST_30_DAYS&errorType=ANR'
GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5115057263789938963#AndroidMetricsErrorsPlace:p=com.bongolight.pixelcoloring&appid=4973594308926896530&lastReportedRange=LAST_60_DAYS&errorType=ANR'
GOOGLEPLAY_ACCOUNT_NAME = 'wenjie.ma@ihandysoft.com' # TODO 1-googleplay account
GOOGLEPLAY_ACCOUNT_PWD = 'xxx'  # TODO 2-password
APP_VERSION = '46' #TODO 3-Version Number
# APP_VERSION = 'PRODUCTION'
# APP_VERSION = 'ALL'
# APP_VERSION = ' '
# APP_VERSION = '82'

total_anr_count = 0


def login(driver):
    try:
        email_box =  driver.find_element_by_xpath("//input[@type='email']")
        email_box.send_keys(GOOGLEPLAY_ACCOUNT_NAME)
        email_box.send_keys(Keys.ENTER)
        time.sleep(2)
    except:
        pass

    try:
        name_box = driver.find_element_by_xpath("//div[@id='profileIdentifier']")
        name_box.send_keys(GOOGLEPLAY_ACCOUNT_NAME)
        time.sleep(2)
    except:
        pass

    try:
        pwd = driver.find_element_by_xpath("//input[@type='password']")
        pwd.send_keys(GOOGLEPLAY_ACCOUNT_PWD)
    except:
        pass

    try:
        signIn = driver.find_element_by_id("passwordNext")
        print (signIn.text)
        signIn.click()
    except:
        pass


# 可通过修改 url 来选择看对应 app_version anr
def get_url(app_version):
    app_ver_start = GOOGLEPLAY_URL.find('appVersion')
    if app_ver_start != -1:
        app_ver_end = GOOGLEPLAY_URL.find('&', app_ver_start)
    else:
        app_ver_end = -1
    if app_ver_end == -1:
        app_ver_end = len(GOOGLEPLAY_URL)

    if len(app_version.strip()) > 0 and GOOGLEPLAY_URL.find(app_version, app_ver_start, app_ver_end) != -1:
        return GOOGLEPLAY_URL

    if app_version.upper() == 'ALL' or len(app_version.strip()) == 0:
        ver_para = 'appVersion'
    else:
        ver_para = 'appVersion='+app_version

    if app_ver_start >= 0:
        return GOOGLEPLAY_URL[:app_ver_start] + ver_para + GOOGLEPLAY_URL[app_ver_end:]
    else:
        return GOOGLEPLAY_URL + '&' + ver_para


def get_data_type_value(data_type, page_source, start, end, reversed = False):
    if reversed:
        pos = page_source.rfind(data_type, start, end)
    else:
        pos = page_source.find(data_type, start, end)
    if pos == -1:
        return ""

    right_angle_quote_pos = page_source.find('>', pos, end)
    if right_angle_quote_pos == -1:
        return ""

    left_angle_quote_pos = page_source.find('<', right_angle_quote_pos, end)
    if left_angle_quote_pos == -1:
        return ""

    str = page_source[right_angle_quote_pos+1:left_angle_quote_pos]
    return str.strip()


def get_attribute_value(attribute, page_source, start, end, reversed = False):
    pass


def write_current_page(driver, writer):
    global total_anr_count
    page_source = driver.page_source
    error_desc_const = 'errorDescription'
    current_element_start = 0
    next_element_start = 0

    # 考虑到可扩展性，计划写成找到所有 errorDescription 节点，再根据 page_source 找相邻属性，这样想加功能方便点
    all_error_descs = driver.find_elements_by_xpath("//p[@data-type='errorDescription']")

    for i in range(0, len(all_error_descs)):
        curr_desc = all_error_descs[i].text

        if next_element_start > 0:
            current_element_start = next_element_start
        else:
            current_element_start = page_source.find(curr_desc, current_element_start)
            # 有时候会找不到，加个保护
            if current_element_start == -1:
                current_element_start = page_source.find(error_desc_const, current_element_start)

        if i == len(all_error_descs) -1:
            next_element_start = len(page_source) - 1
        else:
            next_element_start = page_source.find(all_error_descs[i+1].text, current_element_start + len(error_desc_const))
            # 有时候会找不到，加个保护
            if next_element_start == -1:
                next_element_start = page_source.find(error_desc_const, current_element_start + len(error_desc_const))

        error_location = get_data_type_value('errorLocation', page_source, current_element_start, next_element_start)
        reports_total = get_data_type_value('reportsTotal', page_source, current_element_start, next_element_start)
        num_affected = get_data_type_value('numAffected', page_source, current_element_start, next_element_start)
        new_badge = get_data_type_value('newBadge', page_source, current_element_start, next_element_start)

        if len(new_badge) > 0:
            error_desc = new_badge + '\r\n' + curr_desc + '\r\n' + error_location
        else:
            error_desc = curr_desc + '\r\n' + error_location
        # statisticsDetailStack(all_error_descs[i],error_desc)
        writer.writerow([error_desc, reports_total, num_affected])
        total_anr_count = total_anr_count + 1


if __name__ == '__main__':
    service = service.Service(CHROME_DRIVER_PATH)
    service.start()
    capabilities = {}
    driver = webdriver.Remote(service.service_url, capabilities)
    result_url = get_url(APP_VERSION)
    driver.get(result_url)
    time.sleep(1)

    # 保证是登录状态
    login(driver)

    # 确认已加载
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//p[@data-type='errorDescription']")))
    # print driver.page_source

    # 写文件准备
    csv.register_dialect('myDialect', delimiter=',', lineterminator='\r\n')
    csvfile = open('454new-anr_'+APP_VERSION + '.csv', 'wb')
    csvfile.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(csvfile, dialect='myDialect')
    writer.writerow([u'问题时机描述'.encode('utf8'), u'发生次数'.encode('utf8'), u'影响用户数'.encode('utf8'),u'stack'.encode('utf8')])

    while 1:
        write_current_page(driver, writer)

        try:
            next_page_btn = driver.find_element_by_xpath("//button[@aria-label='Next page']")
            if next_page_btn.is_enabled():
               next_page_btn.click()
               WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//p[@data-type='errorDescription']")))
               time.sleep(0.01)
            else:
               break
        except:
            break

    csvfile.close()
    print('for version {}, the total count of anr : {}'.format(APP_VERSION, total_anr_count))
