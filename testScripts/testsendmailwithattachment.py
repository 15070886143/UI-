#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 10:21
# @Author  : Aries
# @Site    : 
# @File    : testsendmailwithattachment.py
# @Software: PyCharm
from DataDrivenFrameWork.action.pageaction import *
from DataDrivenFrameWork.config.varconfig import *
import time
import unittest
from Apitest.common import HTMLTestRunner_Chart
class sendlogin(unittest.TestCase):
    def testsendmailwithattachment(self):
        username = assert_pagesour()
        print(u'启动谷歌浏览器')
        #创建谷歌浏览器的实例,调用action的open_browser方法
        open_browser("chrome")
        #最大化浏览器窗口，调用action的方法
        # manmize_browser()
        print(u'访问126网易邮箱登录页...')
        #调取配置文件URL
        visit_url(url)
        #调用action的断言方法
        self.assertIn(u'126网易免费邮--你的专业电子邮局',username)
        print(u'访问126网易免费邮网站成功')
        #调取action方法，定位iframe元素并且切换进去
        waitframetobeavailableandswitchtolt('xpath','//*[@id = "loginDiv"]/iframe')
        #等待两秒
        time.sleep(2)
        #调取action方法定位，并在输入框输入用户名
        input_srting('xpath','//input[@name = "email"]',user)
        print(u'输入的用户账号为',user)
        ##调取action方法定位，并在输入框输入密码
        input_srting('xpath','//input[@name = "password"]',pwd)
        print(u'输入的密码为：', pwd)
        print(u'登陆中请稍后.....')
        #调用action的定位并点击方法
        clicks('id','dologin')
        sleep(3)
        #获取登陆后登陆用户名，调用action方法
        text = getelemen('id','spnUid')
        # 调用action的断言方法
        # assert user in text.text
        self.assertIn('1311375671',username)
        print(u'登陆成功，登陆用户为', text.text)

#     print(u'--------添加联系人---------')
#     # #显示等待通讯录链接页面元素的出现，text()方法获取文本定位
#     notbook = waitvisibilityofelementlocated('xpath','//div[text() = "通讯录"]')
#     #点击通讯录链接
#     clicks('xpath','//div[text() = "通讯录"]')
#     # addclick(notbook)
#     #显示等待新建联系人按钮的出现
#     newbook = waitvisibilityofelementlocated('xpath','//span[text() = "新建联系人"]')
#     #调用点击方法，点击新建联系人按钮
#     addclick(newbook)
#     # clicks('xpath','//span[text() = "新建联系人"]')
#     #调用输入数据并发送方法
#     input_srting('xpath','//input[@id = "input_N"]','杨盼1')
#     input_srting('xpath','//*[@id = "iaddress_MAIL_wrap"]//input',usere_mail)
#     #设为星际联系人
#     clicks('xpath','//span[text() = "设为星标联系人"]')
#     # 获取手机号码
#     input_srting('xpath','//*[@id = "iaddress_TEL_wrap"]//input','15070886143')
#     #输入备注信息
#     input_srting('xpath','//textarea[@id = "input_DETAIL"]',u'我自己的朋友，做自动化测试用的数据')
#     #点击确认保存
#     clicks('xpath','//span[text() = "确 定"]')
#     #等待两秒加载完成
#     time.sleep(2)
#     #断言页面返回的联系人是否在page_source源代码中，page_source：获取页面源代码信息
#     assert_string_in_pagesource(u'1311375671')
#     print(u'添加联系人成功')
#     time.sleep(2)
#     # 点击首页并进入
#     clicks('xpath','//div[. = "首页"]')
#     time.sleep(2)
#     #显示等待元素的出现
#     writebook =  waitvisibilityofelementlocated('xpath','//span[text() = "写 信"]')
#     addclick(writebook)
#     # clicks('xpath','//span[text() = "写 信"]')
#     print(u'------------开始写信-------------')
#     #contains()为模糊匹配定位方法
#     time.sleep(2)
#     #定位并发送接受者
#     input_srting('xpath','//div[contains(@id,"_mail_emailinput")]/input','1311375671@qq.com')
#     #定位主题元素并调用方法进行发送
#     input_srting('xpath','//div[@aria-label="邮件主题输入框，请输入邮件主题"]/input',u'杨盼发的新邮件（自动化测试）')
#     #调用设置和获取剪贴板内容的方法
#     # paste_set_get(text_path)
#     #发送附件到input
#     input_srting('xpath','//*[contains(@id,"_attachBrowser")]/input',text_path)
#     #显示等待上传完成
#     logingpath = waitvisibilityofelementlocated('xpath','//span[text() = "上传完成"]')
#     time.sleep(2)
#     #断言是否上传完成
#     assert_string_in_pagesource(logingpath.text)
#     print('上传完成')
#     #调用模拟ctrl+v操作方法
#     # paste_copy()
#     # time.sleep(1)
#     # #调用模拟键盘center操作
#     # paste_enter_key()
#     #切换进入iframe
#     waitframetobeavailableandswitchtolt('xpath','//iframe[@tabindex="1"]')
#     #定位输入框并发送要输入的内容
#     input_srting('xpath','/html/body',u'发给自己的一封信')
#     #切出邮件正文的iframe框
#     switch_to_content()
#     print(u'写信完成')
#     time.sleep(2)
#     #定位发送元素，并进行点击操作方法
#     clicks('xpath','//footer//span[text() = "发送"]')
#     print(u'开始发送邮件...........')
#     time.sleep(2)
#     assert_string_in_pagesource(u'发送成功')
#     print(u'邮件发送成功')
#     time.sleep(1)
if __name__ == '__main__':
    unittest.main()