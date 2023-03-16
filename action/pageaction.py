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
import traceback
import time
import unittest
import random
import pytesseract
from PIL import Image
from PIL import ImageGrab
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
#参数：1：定位方式，2：定位属性值，3：要输入的值
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


#获取多个页面元素对象
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
#获取页面标题
def title(*args):
    global driver
    try:
        return driver.title
    except Exception as e:
        raise e
#获取属性值
def attribute(locationtype,locatorexpression,assging):
    global driver
    try:
        return str(locationtype.get_attribute(locatorexpression))
    except Exception as e:
        raise e
#获取页面源代码
def getpagesource(*args):
    global driver
    try:
        return driver.page_source
    except Exception as e:
        raise  e

#切换进入frame
#参数一：定位方式，二定位属性值
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
#单独截图
def quanping_jietu(*args):
    global driver
    #存放地址
    image = parentdifpath + '\\image\\'+'jietu.png'
    try:
        #开始截图
        driver.get_screenshot_as_file(image)
        print('全屏截图成功')
    except Exception as e:
        raise e
#指定元素进行截图，保存
def zidingyi_jietu(locatetype,locatorexpression,*args):
    try:
        element =waitUtil.visibilityofelementlocated(locatetype,locatorexpression)
        # 获取验证码坐标
        locations = element.location
        # 获取大小
        sizes = element.size
        print(f'元素坐标和大小{locations} {sizes}')
        #先截取全图
        quanping_jietu()
        #获取元素横坐标
        left = element.location['x']
        #获取元素纵坐标
        top = element.location['y']
        #获取横坐标+宽度=左边到右边的宽度坐标
        right = element.location['x'] + element.size['width']
        # 获取纵坐标+高度=上边到下边边的高度坐标
        bottom = element.location['y'] + element.size['height']
        #合并成元祖
        boxx = (left, top, right, bottom)
        #打开截图图片
        im = Image.open(u'../image/jietu.png')
        #crop裁剪方法，对合并的坐标进行截图，并保存
        im = im.crop(boxx)
        im.save(u'../image/jietu.png')
        print('指定区域截图成功')
    except Exception as e:
        raise e
def waitpresenceofelementlocated(locationtype,locatorexpression,*args):
    '''
        显示等待页面元素的出现，但不一定可见，存在返回页面元素对象
    '''
    try:
        return waitUtil.presenceofelementlocated(locationtype,locatorexpression)
    except Exception as e:
        raise e

#参数一：定位方式，二定位属性值
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

##随机生成手机号码
def phoneNORandomGenerator():
    prelist=["130","131","132","133","134","135","136","137","138",
             "139","147","150","151","152","153","155","156","157",
             "158","159","186","187","188"]
    return random.choice(prelist) + "".join(
        random.choice("0123456789") for _ in range(8)
    )
#刷新页面方法
def refresh():
    global driver
    try:
        driver.refresh()
        print('刷新页面成功')
    except Exception as e:
        raise e

#页面前进
def forward():
    global driver
    try:
        driver.forward()
    except Exception as e:
        raise  e
#页面后退
def back():
    global driver
    try:
        driver.back()
    except Exception as e:
        raise  e
#退出浏览器
def quit():
    global driver
    try:
        driver.quit()
        print('退出浏览器成功')
    except Exception as e:
        print(u'退出浏览器异常')
        traceback.print_exc()
#清除浏览器缓存
def de_cookies():
    global driver
    try:
        #获取浏览器的cookies
        cookies = driver.get_cookies()
        print("main: cookies = {cookies}")
        #开始清除
        driver.delete_all_cookies()
    except Exception as e:
        raise e

#断言页面属性值是否存在
#第一个参数页面对象，第二个页面属性
def assert_attribute(locationtype,locatorexpression):
    global driver
    #从对象中获取该属性值
    assert_attrbute = str(locationtype.get_attribute(locatorexpression))
    #从该对象获取HTML源代码
    attrbutehtml = str(locationtype.get_attribute('outerHTML'))
    try:
        #检查属性值是否在该源代码中
        assert assert_attrbute in attrbutehtml
        print(f'断言成功，页面存在该元素，页面返回元素和属性值 [0{locatorexpression}="{assert_attrbute}"]')
    except Exception as e:

        print(
            f'断言失败，页面不存在该元素，期望结果:{locatorexpression}，实际结果:{assert_attrbute}，请进入浏览器打开F12进行定位！'
        )


#获取整个文档的HTML对象，比page_source要好
#第一个参数获取指定的对象，第二个获取要检查的值也就是断言该值是否出现在页面
def assert_get_html(locationtype,assertstring):
    global driver
    try:
        #获取dom对象下所有元素和标签
        html = getelement(driver,'xpath','//*')
        #获取所有HTML源文件
        html_attr = str(html.get_attribute('outerHTML'))
        #获取该对象的HTML源代码
        attrbutehtml = str(locationtype.get_attribute('outerHTML'))
        #检查传入的参数是否在页面中
        assert assertstring in html_attr
        print(f'断言成功，页面源代码包含元素：{assertstring},可在该代码中查看：{attrbutehtml}')
    except Exception as e:
        print(f'断言失败，页面源代码不存在 “{assertstring}” 元素，请手动检查页面！', e)




#断言页面元素是否存在某关键字或者关键字符串
def assert_string_in_pagesource(assertstring,*args):
    global driver
    try:
        #断言页面元素是否在页面显示，如果不存在，抛出格式化后的信息%s格式化字符串，否则抛出异常
        assert (
            assertstring in driver.page_source
        ), f'{assertstring} not found in page source!'
        print(u'断言成功')
    except AssertionError as e:
        print(u'断言失败')
        raise AssertionError(e)
    except Exception as e:
        print(u'断言失败')
        raise e

#断言页面标题是否存在给定的关键字符串
def assert_title(titlestr,*args):
    global driver
    try:
        #断言页面的标题是否与预期一致
        assert titlestr in driver.title, f'{titlestr} not found in title!'
        print(u'断言成功')
    except AssertionError as e:
        print(u'断言失败')
        raise AssertionError(e)
    except Exception as e:
        print(u'断言失败')
        raise e
# if __name__ == '__main__':
#     capture_screen()