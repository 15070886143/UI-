#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:21
# @Author  : Aries
# @Site    : 
# @File    : testsendmailwithattachment.py
# @Software: PyCharm
from DataDrivenFrameWork.action.pageaction import *
from DataDrivenFrameWork.config.varconfig import *
from DataDrivenFrameWork.config.varconfig import mylog
from DataDrivenFrameWork.util.dirandtime import *
from Apitest.common import HTMLTestRunner_Chart
import time
import unittest
import random
import pytesseract
from PIL import Image
from PIL import ImageGrab
from selenium import  webdriver

class share(unittest.TestCase):
    yanzm = getcurrenttimes()
    yanzm = int(yanzm)
    # @unittest.skip('PC暂时不测试')  # 忽略该用例
    @classmethod
    def setUp(cls):
        print(u'启动谷歌浏览器--开始分享注册测试')
        mylog.info(u'启动谷歌浏览器--开始分享注册测试')
        open_browser('chrome')
        #最大化浏览器窗口，调用action的方法
        manmize_browser()
        mylog.info('窗口最大化成功')
        print(u'访问大咖直播间......')
        #调取配置文件URL
    #PC端分享注册自动化
    def cgtanchang(self):
        if self:
            print('注册弹出窗口成功,')
            capture_screen()
        else:
            print('弹窗失败，请清除缓存再继续执行')
    ##单个PC注册
    # @unittest.skip('PC暂时不测试') #忽略该用例
    def test_PC(self,num,PC_url):
        visit_url(PC_url)
        # 调用action的断言方法
        print(u'进入直播间成功')
        mylog.info(u'进入直播间成功')
        mylog.info('-------正在执行PC端注册自动化用例------')
        print('-------正在执行PC端注册自动化用例------')
        try:
            req = 0
            for i in range(1,num):
                if req<i:
                    req += 1
                    #单机登陆
                    getelemen('xpath','//span[text()="登录"]').click()
                    #获取页面短信登陆按钮并点击
                    sleep(1)
                    waitvisibilityofelementlocated('xpath','//span[@class="msglogin"]').click()
                    #显示等待弹窗出现并断言
                    writephone = waitvisibilityofelementlocated('xpath','//input[@id="phonemsg"]')
                    #获取手机号码
                    phone =phoneNORandomGenerator()
                    # 调用手机号码生成放法，并输入
                    writephone.send_keys(phone)
                    mylog.info(phone)
                    print(phone)
                    #写入验证码
                    writepwd = waitvisibilityofelementlocated('xpath','//input[@id="msgsend"]')
                    print(getcurrenttimes)
                    writepwd.send_keys(share.yanzm)
                    #点击登陆
                    getelemen('xpath','//li[@class="dd_zc"]').click()
                    zctcc = waitvisibilityofelementlocated('xpath','//img[@id="imgbtn"]')
                    if zctcc:print('注册弹出窗口成功,')
                    else:print('弹窗失败，请清除缓存再继续执行')
                    share.cgtanchang(zctcc)
                    addclick(zctcc)
                    sleep(2)
                    #获取退出
                    waitvisibilityofelementlocated('xpath','//span[text()="退出"]').click()
                    visit_url(PC_url)
                    print(f'当前是第 {req}次注册，注册成功')
                    mylog.info(f'当前是第 {req}次注册，注册成功')
                elif req == i:
                    print('已经全部执行完毕')
                    mylog.info(f'已全部OK，用例{req}成功')
                    quit()
                else:
                    print('用例执行失败')
        except Exception as e:
            mylog.info(e)
            raise e

    ##多个一起注册测试
    # wap和PC端分享注册自动化
    # @unittest.skip('WAP暂时不测试') #忽略该用例
    def test_wpcs(self,n,m,list_url):
        try:
            sum =0
            for su in range(n,m):
                if sum < su:
                    for i,index in enumerate(list_url):
                        sum +=1
                        # 调用action的断言方法
                        print(f'--正在执行---第{sum}次---WAP注册自动化用例--')
                        visit_url(index)
                        if tanc := waitvisibilityofelementlocated(
                            'xpath', '//div[@id="logindialog"]'
                        ):
                            if tanc:print('弹窗成功')
                        else:
                            print('弹窗失败，请清除缓存再继续执行')
                        #获取手机号码文本框
                        writephone = waitvisibilityofelementlocated('xpath', '//input[@id="loginphone"]')
                        # 获取手机号码
                        phone = phoneNORandomGenerator()
                        # 调用手机号码生成放法，并输入
                        writephone.send_keys(phone)
                        print(phone)
                        mylog.info(phone)
                        # 写入验证码
                        writepwd = waitvisibilityofelementlocated('xpath', '//input[@id="loginmsgcode"]')
                        writepwd.send_keys(share.yanzm)
                        # 点击提交
                        getelemen('xpath', '//span[@id="loginbtn"]').click()
                        queren = waitvisibilityofelementlocated('xpath','//*[@id="dialogSure"]')
                        share.cgtanchang(queren)
                        sleep(1)
                        addclick(queren)
                        print(f'当前是第 {sum}次注册，注册成功')
                        mylog.info(f'当前是第 {sum}次注册，注册成功')
                        #清除cookies
                        de_cookies()
                        sleep(2)
                        visit_url(index)
                elif sum==su:
                    print(f'总共{sum}用例，已经全部执行完毕')
                    mylog.info(f'已全部OK，用例{sum}成功')
                    quit()
                    break
                else:
                    print('注册失败')
                    break

        except Exception as e:
            mylog.info(e)
            raise e
    #单个wap测试
    # @unittest.skip('WAP暂时不测试')  # 忽略该用例
    def test_wap(self,num,WAP_url):
        visit_url(WAP_url)
        # 调用action的断言方法
        print(u'进入直播间成功')
        mylog.info(u'进入直播间成功')
        mylog.info('-------正在执行WAP端注册自动化用例------')
        try:
            req = 0
            for i in range(num):
                if req < i:
                    req += 1
                    # 单机登陆
                    print(f'--正在执行---第{req}次---WAP注册自动化用例--')
                    # 等待弹窗元素出现
                    tanc = waitvisibilityofelementlocated('xpath', '//div[@id="logindialog"]')
                    assert_string_in_pagesource(tanc)
                    if tanc:
                        print('弹窗成功')
                    else:
                        print('弹窗失败，请清除缓存再继续执行')
                    # 获取手机号码文本框
                    writephone = waitvisibilityofelementlocated('xpath', '//input[@id="loginphone"]')
                    # 获取手机号码
                    phone = phoneNORandomGenerator()
                    # 调用手机号码生成放法，并输入
                    writephone.send_keys(phone)
                    print(phone)
                    mylog.info(phone)
                    # 写入验证码
                    writepwd = waitvisibilityofelementlocated('xpath', '//input[@id="loginmsgcode"]')
                    writepwd.send_keys(share.yanzm)
                    # 点击提交
                    getelemen('xpath', '//span[@id="loginbtn"]').click()
                    queren = waitvisibilityofelementlocated('xpath', '//*[@id="dialogSure"]')
                    share.cgtanchang(queren)
                    assert_string_in_pagesource(queren.text)
                    sleep(1)
                    addclick(queren)
                    print(f'当前是第 {req}次注册，注册成功')
                    mylog.info(f'当前是第 {req}次注册，注册成功')
                    # 清除cookies
                    de_cookies()
                    sleep(2)
                    visit_url(WAP_url)
                elif req == i:
                    print('已经全部执行完毕')
                    mylog.info(f'已全部OK，用例{req}成功')
                else:
                    print('用例执行失败')
        except Exception as e:
            mylog.info(e)
            raise e
# def add_case(rule="testsendmailwith*.py"):
#     try:
#         '''加载所有的测试用例'''
#         datapath = os.path.join(parentdifpath,'testScripts')
#         # 定义discover方法的参数
#         discover = unittest.defaultTestLoader.discover(datapath,
#                                                   pattern=rule,)
#         return discover
#     except Exception as e:
#         raise e
#
# def run_case(all_case):
#     try:
#         '''执行所有的用例, 并把结果写入测试报告'''
#         report_path = os.path.join(parentdifpath, "report")
#         # 如果不存在该目录，则创建
#         if not os.path.exists(report_path): os.mkdir(report_path)
#         htmlreport = report_path + r"\result.html"
#         # xlsxreport = reportpath+r"\result.xlsx"
#         print("测试报告生成地址：%s" % htmlreport)
#         fp = open(htmlreport, "wb")
#         runner = HTMLTestRunner_Chart.HTMLTestRunner(
#             stream=fp,
#             title=u'自动化测试报告',
#             description='详细测试用例结果',
#         )
#         # 调用add_case函数返回值
#         runner.run(all_case)
#         # readmail.sendMail(htmlreport,xlsxreport)
#         fp.close()
#     except Exception as e:
#         raise e

if __name__ == '__main__':
    unittest.main()
