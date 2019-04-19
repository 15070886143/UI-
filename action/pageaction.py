#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:49
# @Author  : Aries
# @Site    : 
# @File    : pageaction.py
# @Software: PyCharm
from selenium import  webdriver
from DataDrivenFrameWork.util.waitutil import waitutil
from DataDrivenFrameWork.config.varconfig import *
from DataDrivenFrameWork.util.objectMap import getelement,getelements
from DataDrivenFrameWork.util.clipboardtuil import clipboard
from DataDrivenFrameWork.util.keyboardutil import keyboardkeys
from DataDrivenFrameWork.util.dirandtime import *
from selenium.webdriver.chrome.options import Options
import time
import unittest

#定义全局driver变量
driver = None
#定义全局等待类实例对象
waitUtil = None
def open_browser(browsername,*args):
    #打开浏览器
    global driver,waitUtil #更改函数体内为全局变量
    try:
        #如果打开浏览器为IE，lower（）放大转换成小写
        if browsername.lower() == 'ie':
            driver = webdriver.Ie(executable_path=iedriverpath)
        elif browsername.lower() == 'chrome':
            #创建chrome浏览器的一个options实例对象
            chrome_options = Options()
            #添加屏蔽 ---ignore --certificate-errors提示信息的设置参数项
            chrome_options.add_experimental_option(
                "excludeSwitches",
                ["ignores - certificate - errors"]
            )
            driver = webdriver.Chrome(
                executable_path = chromedriverpath,
                chrome_options = chrome_options
            )
        else:
            driver = webdriver.Firefox(executable_path=firefoxdriverpath)

            #对象创建完之后，创建等待类实例对象
        waitUtil = waitutil(driver)
    except Exception as e:
        raise e


#定位访问某个网站
def visit_url(url,*args):
    global driver
    try:
        driver.get(url)
    except Exception as e:
        raise e

#定义关闭浏览器
def close_browser(*args):
    global driver
    try:
        driver.quit()
    except Exception as e:
        raise  e

##强制等待
def sleep(sleepseconds,*args):
    try:
        #传入时间为int
        time.sleep(int(sleepseconds))
    except Exception as e:
        raise  e

#清除输入框默认内容
def clear(locationtype,locatorexpression,*args):
    global driver
    try:
        #获取页面元素，然后执行清除动作
        getelement(driver,locationtype,locatorexpression).clear()
    except Exception as e:
        raise e

#在页面输入框输入数据
def input_srting(locationtype,locatorexpression,inputcontent):
    global driver
    try:
        #获取页面元素后执行发送信息动作
        getelement(driver,locationtype,locatorexpression).send_keys(inputcontent)

    except Exception as e:
        raise e

def getelemen(locatetype,locatorexpression):
    '''
    获取单个页面元素对象
    '''
    global driver
    try:
        return getelement(driver,locatetype,locatorexpression)
    except Exception as e:
        raise e


#单机页面元素
def getelemens(locationtype,locatorexpression):
    global driver
    try:
        # 获取页面元素后执行点击动作
        return getelements(driver,locationtype,locatorexpression)
    except Exception as e:
        raise e

#单机页面元素
def clicks(locationtype,locatorexpression,*args):
    global driver
    try:
        # 获取页面元素后执行点击动作
        getelement(driver,locationtype,locatorexpression).click()
    except Exception as e:
        raise e
def addclick(locationtype,*args):
    try:
        # 获取页面元素后执行点击动作
        locationtype.click()
    except Exception as e:
        raise e

#断言页面元素是否存在某关键字或者关键字符串
def assert_string_in_pagesource(assertstring,*args):
    global driver
    try:
        #断言页面元素是否在页面显示，如果不存在，抛出格式化后的信息%s格式化字符串，否则抛出异常
        assert assertstring in driver.page_source,\
        u'%s not found in page source!' % assertstring
        print(u'断言成功')
    except AssertionError as e:
        print(u'断言失败')
        raise AssertionError(e)
    except Exception as e:
        print(u'断言失败')
        raise e


# class assert_page_check(unittest.TestCase):
#     def test_assert_string_in_pagesource(self,assertstring):
#         global driver
#         try:
#             # 断言页面元素是否在页面显示，如果不存在，抛出格式化后的信息%s格式化字符串，否则抛出异常
#             self.assertIn(assertstring,driver.page_source),\
#                 u'%s not found in page source!' % assertstring
#             print(u'断言成功')
#         except AssertionError as e:
#             print(u'断言失败')
#             raise AssertionError(e)
#         except Exception as e:
#             print(u'断言失败')
#             raise e

#断言页面标题是否存在给定的关键字符串
def assert_title(titlestr,*args):
    global driver
    try:
        #断言页面的标题是否与预期一致
        assert titlestr in driver.title, \
        u'%s not found in title!' % titlestr
        print(u'断言成功')
    except AssertionError as e:
        print(u'断言失败')
        raise AssertionError(e)
    except Exception as e:
        print(u'断言失败')
        raise e

def assert_pagesour(titlestr,*args):
    global driver
    try:
        #断言页面的标题是否与预期一致
        page = driver.page_source
        return page
    except AssertionError as e:
        print(u'断言失败')
        raise AssertionError(e)
    except Exception as e:
        print(u'断言失败')
        raise e
#获取页面标题
def title(*args):
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e

#获取页面远吗
def getpagesource(*args):
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise  e

#切换进入frame
def switch_to_frame(locationtype,framelocatorexpression,*args):
    global driver
    try:
        driver.switch_to.frame(getelement(
            driver,locationtype,framelocatorexpression
        ))
    except Exception as e:
        print('frame error')
        raise e

#退出frame，回到默认对话框中
def switch_to_content(*args):
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

##模拟ctrl+v操作
def paste_copy(*args):
    try:
        keyboardkeys.towkeys("ctrl","v")
    except Exception as e:
        raise e

 #模拟设置剪贴板和获取剪贴板内容
def paste_set_get(pastestring,*args):
    try:
        clipboard.settext(pastestring)
        time.sleep(1)
        clipboard.gettext()
    except Exception as e:
        raise e

 #模拟tab键
def paste_tab_key(*args):
    try:
        keyboardkeys.onekey("tab")
    except Exception as e:
        raise e

#模拟enter键
def paste_enter_key(*args):
    try:
        keyboardkeys.onekey("enter")
    except Exception as e:
        raise  e

#窗口最大化
def manmize_browser():
    global driver
    try:
        driver.maximize_window()
    except Exception as e:
        raise e

#截取屏幕图片方法
def capture_screen(*args):
    global driver
    # open_browser("chrome")
    # visit_url(url)
    #获取当前时间，精确到毫秒
    currtime = getcurrenttime()
    #拼接异常图片保存的绝对路径和名称
    picnameandcpath = str(createcurrentdatedir()) + '\\'+ str(currtime) + '.png'
    try:
        #截取屏幕图片，并保存为本地文件,get_screenshot_as_file截取方法,replace把旧数据替换成新数据
        driver.get_screenshot_as_file(picnameandcpath.replace('\\',r'\\'))
        print('截图成功！')
    except Exception as e:
        raise e
    else:
        return picnameandcpath

def waitpresenceofelementlocated(locationtype,locatorexpression,*args):
    '''
        显示等待页面元素的出现，但不一定可见，存在返回页面元素对象
    '''
    try:
        return waitUtil.presenceofelementlocated(locationtype,locatorexpression)
    except Exception as e:
        raise e

def waitframetobeavailableandswitchtolt(locationtype,locatorexpression,*args):
    '''
        检查frame是否 存在，存在则切换进入frame控件中
    '''
    try:
        return waitUtil.frametobeavailableandswitchtolt(locationtype,locatorexpression)
    except Exception as e:
        raise  e

def waitvisibilityofelementlocated(locationtype,locatorexpression,*args):
    '''
    显示等待页面元素出现在DOM中，并且可见，存在返回页面对象
    '''
    try:
       return waitUtil.visibilityofelementlocated(locationtype,locatorexpression)
    except Exception as e:
        raise  e


if __name__ == '__main__':
    capture_screen()