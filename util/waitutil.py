#!usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DataDrivenFrameWork.util.objectMap import *
from DataDrivenFrameWork.action.pageaction import *
from DataDrivenFrameWork.config.varconfig import *
import time
class waitutil(object):
    def __init__(self,driver):
        #创建并映射定位方式的字典对象
        self.locationtypeDict={
            "xpath":By.XPATH,
            "id":By.ID,
            "name":By.NAME,
            "css_selector":By.CSS_SELECTOR,
            "class_name":By.CLASS_NAME,
            "tag_name":By.TAG_NAME,
            "link_text":By.LINK_TEXT,
            "partial_link_text":By.PARTIAL_LINK_TEXT
        }
        #初始化driver对象
        self.driver = driver
        #创建显示等待实例对象
        self.wait = WebDriverWait(self.driver,10)
    def presenceofelementlocated(self,locatormethod,locatorexpression):
        '显示等待页面元素出现在DOM中，单不一定可见，存在则返回该页面元素对象'
        try:
            element = self.wait.until(
                EC.presence_of_element_located((self.locationtypeDict[locatormethod.lower()],locatorexpression)))
            return element
        except Exception as e:
            print(u'不一定可见元素未找到定位方式，请确认定位方法是否正确!',e)
    def frametobeavailableandswitchtolt(self,locationtype,locatorexpression):
        '检查frame是否 存在，存在则切换进入frame控件中'
        try:
             element = self.wait.until(
                EC.frame_to_be_available_and_switch_to_it((
                    self.locationtypeDict[locationtype],locatorexpression)))
             return element
        except Exception as e:
            print('定位超时，frame不存在，切入失败',e)
    def visibilityofelementlocated(self,locationtype,locatorexpression):
        '显示等待页面元素出现在DOM中，并且可见，存在返回页面对象'
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((
                    self.locationtypeDict[locationtype.lower()],locatorexpression)))
            return element
        except Exception as e:
            print(u'可见元素未找到定位方式，请确认定位方法是否正确!',e)

if __name__=='__main__':
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    driver = webdriver.Chrome(executable_path='../Browser driver/chromedriver.exe')
    driver.get('http://email.126.com/')
    waitutil = waitutil(driver)
    #第一种定位iframe方法
    # iframe = waitutil.visibilityofelementlocated('tag_name','iframe')
    #第二种定位iframe方法
    # iframe = getelement(driver,'xpath','//*[@id = "loginDiv"]/iframe')
    #第三种iframe定位方法

    waitutil.frametobeavailableandswitchtolt("xpath",'//*[@id = "loginDiv"]/iframe')
    #切换进入iframe框架
    # driver.switch_to.frame(iframe)
    time.sleep(2)
    # inputEmail = input('请输入邮箱账号或手机号码：')
    # inputpwd = input('请输入密码：')
    #定位email文本框
    email = getelement(driver,'xpath','//*[@name = "email"]')
    #发送用户账号
    email.send_keys('yp1311375671')
    #定位密码框
    password = getelement(driver,'xpath','//*[@name = "password"]')
    #发送密码
    password.send_keys('19930724')
    time.sleep(1)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    loginpass = getobject('id','spnUid')
    logtext = loginpass.text()
    assert user in logtext
    print(u'登陆成功，登陆用户为',logtext)
    #获取email属性
    #emailText = email.get_attribute('data-placeholder')
    #打印属性值
    #print(emailText)



    driver.quit()

    #title_is：判断当前页面的title是否等于预期
    # title_contains：判断当前页面的title是否包含预期字符串
    # presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见
    # visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
    # visibility_of：跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
    # presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
    # text_to_be_present_in_element：判断某个元素中的text是否 包含 了预期的字符串
    # text_to_be_present_in_element_value：判断某个元素中的value属性是否包含了预期的字符串
    # frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
    # invisibility_of_element_located：判断某个元素中是否不存在于dom树或不可见
    # element_to_be_clickable - it is Displayed and Enabled：判断某个元素中是否可见并且是enable的，这样的话才叫clickable
    # staleness_of：等某个元素从dom树中移除，注意，这个方法也是返回True或False
    # element_to_be_selected：判断某个元素是否被选中了,一般用在下拉列表
    # element_located_to_be_selected
    # element_selection_state_to_be：判断某个元素的选中状态是否符合预期
    # element_located_selection_state_to_be：跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
    # alert_is_present：判断页面上是否存在alert
