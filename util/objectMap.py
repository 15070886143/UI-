#encoding = utg-8
from selenium.webdriver.support.ui import WebDriverWait


import time
#获取单个页面元素对象
def getelement(driver,locatetype,locatorexpression):
    try:
        return WebDriverWait(driver, 30).until(
            lambda x: x.find_element(by=locatetype, value=locatorexpression)
        )
    except Exception as e:
        raise e
#获取多个页面元素对象
def getelements(driver,locatetype,locatorexpression):
    try:
        return WebDriverWait(driver, 30).until(
            lambda x: x.find_elements(by=locatetype, value=locatorexpression)
        )
    except Exception as e:
        raise e



