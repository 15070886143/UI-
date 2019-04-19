#encoding = utg-8
from selenium.webdriver.support.ui import WebDriverWait


import time
#获取单个页面元素对象
def getelement(driver,locatetype,locatorexpression):
    try:
        #下面两句：创建对象，没30毫秒监控一次，如果监控到，执行下一步，否则一直等待，知道抛出异常
        element = WebDriverWait(driver,30).until\
            (lambda x: x.find_element(by=locatetype,value=locatorexpression))
        return element
    except Exception as e:
        raise e
#获取多个页面元素对象
def getelements(driver,locatetype,locatorexpression):
    try:
        #下面两句：创建对象，没30毫秒监控一次，如果监控到，执行下一步，否则一直等待，知道抛出异常
        elements = WebDriverWait(driver,30).until\
            (lambda x: x.find_elements(by=locatetype,value=locatorexpression))
        return elements
    except Exception as e:
        raise e



