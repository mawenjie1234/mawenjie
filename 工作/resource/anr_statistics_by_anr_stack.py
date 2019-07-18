# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


import selenium.webdriver.chrome.service as service
import csv

CHROME_DRIVER_PATH = '/Users/hd-imac/Downloads/chromedriver'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.zerogravity.booster&appid=4972385200317449506&lastReportedRange=LAST_60_DAYS&errorType=ANR&installSource=INSTALLED_FROM_PLAY'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=8443677975547023839#AndroidMetricsErrorsPlace:p=com.pixel.art.coloring.color.by.number&appid=4975206524895984119&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5903900490511815440#AndroidMetricsErrorsPlace:p=com.oneapp.max.cleaner.booster&appid=4975465364472100027&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5115057263789938963#AndroidMetricsErrorsPlace:p=com.pixel.art.coloring.color.by.number&appid=4975206524895984119&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5115057263789938963#AndroidMetricsErrorsPlace:p=com.bongolight.pixelcoloring&appid=4973594308926896530&lastReportedRange=LAST_30_DAYS&errorType=ANR'
# GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=8443677975547023839#AndroidMetricsErrorsPlace:p=com.zerogravity.booster&appid=4972385200317449506&lastReportedRange=LAST_30_DAYS&errorType=ANR'
GOOGLEPLAY_URL = 'https://play.google.com/apps/publish/?account=5115057263789938963#AndroidMetricsErrorsPlace:p=com.bongolight.pixelcoloring&appid=4973594308926896530&lastReportedRange=LAST_60_DAYS&errorType=ANR'
GOOGLEPLAY_ACCOUNT_NAME = 'wenjie.ma@ihandysoft.com' # TODO 1-googleplay account
GOOGLEPLAY_ACCOUNT_PWD = 'xxx'  # TODO 2-password
APP_VERSION = '57' #TODO 3-Version Number
FILTER_BY_ANR_TYPE = 1
ANR_TYPE_NAME = 'Input'
DEBUG_ONCE = 0
FILTER_DUPLICATE = 0
# APP_VERSION = 'PRODUCTION'
# APP_VERSION = 'ALL'
# APP_VERSION = ' 'saveStack

total_anr_count = 0
stack_href = []
stack_info = [('REPORT_TIME','DEVICE','PAGE_NO','Report_no_in_href','ANR_Type', 'Main_thread_status', 'issue_scene', 'issue_reason','full_stack','href')]
happen_time = ''

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
        print signIn.text
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
        writer.writerow([error_desc, reports_total, num_affected])
        total_anr_count = total_anr_count + 1

def statictis_all_href():
    print ("+++++++++++statictis_all_href")
    stack_href = []
    page_index = 1
    while 1:
        write_current_page(driver, writer)
        all_error_descs = driver.find_elements_by_xpath("//p[@data-type='errorDescription']")
        for i in range(0, len(all_error_descs)):
            curr_desc = all_error_descs[i].text
            print ('---' + curr_desc)
            if FILTER_BY_ANR_TYPE and curr_desc.find(ANR_TYPE_NAME) < 0:
                continue
            href = all_error_descs[i].find_element_by_xpath('..').get_attribute('href')
            report_totals = all_error_descs[i].find_element_by_xpath('../../../../../td[2]/div[1]/p[1]')
            print  ('href:' + href)
            print ('report_totals:' + report_totals.text)
            # print ('href:' + href)
            stack_href.append(str(page_index) + '|' + href+'|' + report_totals.text+'|'+curr_desc)
            if DEBUG_ONCE:
               break  # TEST once
        if DEBUG_ONCE:
           break  # TEST once
        try:
            next_page_btn = driver.find_element_by_xpath("//button[@aria-label='Next page']")
            if next_page_btn.is_enabled():
               next_page_btn.click()
               WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//p[@data-type='errorDescription']")))
               time.sleep(0.01)
               page_index +=1
            else:
                break
        except:
            break
    return stack_href

def get_reportExtra():
    elements = driver.find_elements_by_xpath(".//*[@class='gwt-Label']")
    report_time = ''
    device_info = ''
    ele_text = ''
    # print '==============invoke the get_reportExtra method:'+str(len(elements))
    for index in range(0, len(elements)):
        ele = elements[index]
        ele_text = ele.text
        if ele_text.find('app version') < 0:
           continue
        report_time = ele_text
        try:
            device_android = ele.find_element_by_xpath('../../div[1]/div[1]/div[1]')
            device_info = device_android.text
        except NoSuchElementException as msg:
            print u"查找元素异常%s" % msg
            break
        break
    report_extra = [report_time,device_info]
    print ('report_time:' + report_time + ',device_information:' + device_info)
    return report_extra


def statisticsDetailStack():
    print ("+++++++++++statisticsDetailStack")
    stack_href = statictis_all_href()

    print('******:stack_href length:' + str(len(stack_href)))
    href_value = ''
    last_href_value = ''
    page_no = -1
    report_no = 1
    last_page_no = -1
    for index in range(0, len(stack_href)):
        stack_href[index] = stack_href[index].replace(',','')
        try:
            page_no = stack_href[index].split('|')[0]
            href_value = stack_href[index].split('|')[1]
            report_num = int(stack_href[index].split('|')[2])
            anr_type = stack_href[index].split('|')[3]
        except:
            print ('except')
        if href_value ==last_href_value:
           print ('!!!!!!str compare equals----------'+ href_value)
           # break;
        last_href_value = href_value
        if last_page_no != int(page_no) :
           last_page_no = page_no
           report_no = 1
        # href_value = "https://play.google.com/apps/publish/?account=8505122062204140606#AndroidMetricsErrorsPlace:p=com.zerogravity.booster&appid=4972385200317449506&lastReportedRange=LAST_60_DAYS&errorType=ANR&installSource=INSTALLED_FROM_ANYWHERE&appVersion=93&clusterName=apps/com.zerogravity.booster/clusters/163c6382&detailsAppVersion=93&detailsInstallSource=INSTALLED_FROM_ANYWHERE"
        driver.get(href_value)
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@class='gwt-HTML']")))
        page = 1
        while 1:
            # read the data of each page
            stack = []
            print 'page ' +str(page)
            elements = driver.find_elements_by_xpath(".//*[@class='gwt-HTML']")
            print ('elements:' + str(len(elements)))
            report_extra = get_reportExtra()
            ele_text = ''
            for index in range(0, len(elements)):
                ele = elements[index]
                ele_text = ele.text
                # only read the stack of the main thread
                if ele_text.find('tid=1') < 0:
                    continue
                stack.append(ele.text)
                print ('###############page_no:'+page_no+',report_no:'+str(report_no)+'\r\n----' + ele_text)
                i = 1
                while 1:
                    # read all the detail stacks of the main thread
                    try:
                        stack_ele = ele.find_element_by_xpath('../div[2]/div[' + str(i) + ']/div[2]/div[1]')
                        stack.append(stack_ele.text)
                        print '----' + stack_ele.text
                    except NoSuchElementException as msg:
                        print u"查找元素异常%s" % msg
                        break
                    except StaleElementReferenceException as msg1:
                        print u"StaleElementReferenceException%s" % msg1
                        break
                    i +=1
                break
            analysisStack(ele_text,stack,href_value,page_no,str(report_no),report_extra,anr_type)
            if DEBUG_ONCE:
               break  # TEST once
            next_page_exists = navigateToNextPage("//*[@class='gwt-HTML']")
            # if not next_page_exists:
            #    # try to re-navigate to next page for 4 times when fail to navigate the next page
            #    for dex in range(4):
            #        time.sleep(1)
            #        print 'try the ' +str(dex+1) +' times to re-navigate to next page:'
            #        next_page_exists = navigateToNextPage("//*[@class='gwt-HTML']")
            #        if not next_page_exists:
            #            continue
            #        break
            print ('=====================next_page_exists:'+ str(next_page_exists))
            if not next_page_exists:
                break
            if page >= report_num:
                print ('!!!!!!!page > report_num' + str(page) +","+ str(report_num))
                break
            page += 1
            report_no +=1
        if DEBUG_ONCE:
           break #TEST once
        # break


def analysisStack(main_text,element_array,href,page_no,report_no,report_extra,anr_type):
    print ("+++++++++++analysisStack：element_array length:" + str(len(element_array)))
    split_array = main_text.split()
    if len(split_array) < 4:
        print ('fail to get the td status of th main thread:' + main_text)
        return
    main_status = split_array[3]
    pc_end_index = -1
    msg_end_index = -1
    looper_start = -1
    google_facebook_index = -1
    for i in range(0, len(element_array)):
        if element_array[i].find('  pc') > 0:
            pc_end_index = i

        if (google_facebook_index < 0) and ((element_array[i].find('google') > 0) or (element_array[i].find('facebook') > 0)):
            google_facebook_index = i
        if msg_end_index < 0:
           if (element_array[i].find('nativePollOnce') > 0) or (element_array[i].find('dispatchMessage') > 0) or (element_array[i].find('handleCallback') > 0):
               msg_end_index = i

        if (looper_start < 0) and (element_array[i].find('CrashGuard') > 0):
            looper_start = i
            break
    print "pc:"+ str(pc_end_index)+ ",google_facebook:" + str(google_facebook_index)+ ",msg:" + str(msg_end_index) + ",looper:" + str(looper_start)
    reason_stack = []
    reason_index = pc_end_index + 1
    reason_end_index = 0
    if pc_end_index > 0:
        reason_end_index = pc_end_index + 5
        if reason_end_index < google_facebook_index:
            reason_end_index = google_facebook_index
        while reason_index <= reason_end_index:
            if reason_index >= len(element_array):
                break
            print ("----:reason" + element_array[reason_index])
            reason_stack.append(element_array[reason_index])
            reason_index += 1
    scene_stack = []
    scene_index = msg_end_index - 5
    scene_end_index = msg_end_index - 1
    if scene_index < 0:
       scene_stack.append('android.os.Looper.loop')
       print '----scene is empty'
    else:
        if (google_facebook_index >=0) and (scene_index > google_facebook_index):
            scene_index = google_facebook_index
        while scene_index <= scene_end_index:
            if scene_index >= len(element_array):
                break
            print "scene index:" + str(scene_index)
            print "scene endindex:" + str(scene_end_index)
            print ("----:scene" + element_array[scene_index])
            scene_stack.append(element_array[scene_index])
            scene_index += 1
    saveStack(main_status,reason_stack,scene_stack,element_array,href,page_no,report_no,report_extra,anr_type)



def saveStack(main_status,reason_stack,scene_stack,element_array,href,page_no,report_no,report_extra,anr_type):
    global happen_time
    print ("+++++++++++saveStack")
    scene = '\n'.join(scene_stack)
    reason = '\n'.join(reason_stack)
    check_duplicate = str(report_no) + '==='+report_extra[0] +'====' +href
    if DEBUG_ONCE:
       print ('happen_time:' + happen_time+',check:' + check_duplicate)
    if FILTER_DUPLICATE and happen_time.find(check_duplicate) > 0:
        if DEBUG_ONCE:
           print "onnonononononono++++++++="+ check_duplicate
        return
    # stack_info = [('ANR_Type', 'Main_thread_status', 'issue_scene', 'issue_reason')]
    is_exist_report = False
    # for stack in stack_info:
    global stack_info
    stack_info = []
    stack_info.append((report_extra[0],report_extra[1],page_no,report_no,anr_type,main_status,scene,reason,'\n'.join(element_array),href))
    happen_time += check_duplicate
    # file_pref =
    csvfile = open('454new----save-stack-'+ANR_TYPE_NAME + APP_VERSION +'.csv', 'a')
    writer = csv.writer(csvfile)
    try:
       writer.writerows(stack_info)
    except:
        print 'fail to write'
    finally:
        csvfile.close()
    print ('saveStack:OK')

def navigateToNextPage(next_page_tag):
    print ("+++++++++++navigateToNextPage")
    try:
        next_page_btn = driver.find_element_by_xpath("//button[@aria-label='Next page']")
        if next_page_btn.is_enabled():
           next_page_btn.click()
           WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, next_page_tag)))
           time.sleep(3)
           return True
        else:
           print 'page is disabled'
           return False
    except:
        return False

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
    csvfile = open('anr.csv', 'wb')
    csvfile.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(csvfile, dialect='myDialect')
    writer.writerow([u'问题时机描述'.encode('utf8'), u'发生次数'.encode('utf8'), u'影响用户数'.encode('utf8'),u'stack'.encode('utf8')])
    #
    # while 1:
    #     write_current_page(driver, writer)
    #     next_page_btn = driver.find_element_by_xpath("//button[@aria-label='Next page']")
    #     if next_page_btn.is_enabled():
    #         next_page_btn.click()
    #         WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//p[@data-type='errorDescription']")))
    #         time.sleep(0.01)
    #     else:
    #         break
    statisticsDetailStack()
    csvfile.close()
    print('for version {}, the total count of anr : {}'.format(APP_VERSION, total_anr_count))
