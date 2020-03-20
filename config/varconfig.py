#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 13:57
# @Author  : Aries
# @Site    : 
# @File    : varconfig.py
# @Software: PyCharm\

from untitled.DataDrivenFrameWork.util.readExcel import ParseExcel
import os
import openpyxl
from openpyxl.styles import Font, colors, Alignment
from untitled.DataDrivenFrameWork.util.logger import *
# from DataDrivenFrameWork.action.pageaction import assert_page_check
#实例化断言方法
# check = assert_page_check()
#调取log的方法
mylog = logger().getlog()
#邮箱登陆账号
user = 'yp1311375671'
pwd = '19930724'
url = 'https://www.126.com/'
usere_mail = '1311375671@qq.com'
#设置浏览器驱动
iedriverpath = '../Browser driver/chromedriver.exe'
chromedriverpath = '../Browser driver/chromedriver.exe'
firefoxdriverpath = '../Browser driver/geckodriver.exe'


#获取目录结构os获取当前父目录的绝对路径,返回上一级目录，如config这一级别
parentdifpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#异常目录存放地址
screenpicyuresdir = parentdifpath + '\\exceptionpictures\\'

#发送邮件时，上传的附件地址
txtpath = os.path.join(parentdifpath, 'Enclosure')
text_path = os.path.join(txtpath,'a.txt')

#测试数据文件存放地址
datafilepath = parentdifpath + u'\\textdata\\126邮箱创建联系人并发送邮件.xlsx'

#创建Excel解析对象

excelobj = ParseExcel()

#讲Excel数据文件加载到内存

excelobj.loadWoekBook(datafilepath)

#设置excel背景颜色
colordict = [colors.GREEN, colors.RED]



#测试数据文件中，测试用例表 中部分对应的数字序号

testcase_testcasename = 1 # 用例名称
testcase_frameworkname = 3 #调用框架类型
testcase_datasourcesheetname = 4 #用例步骤sheet名
testcase_testsheetname = 5 # 数据驱动的数据源sheet名
testcase_isexcute = 6 # 是否执行
testcase_runtime = 7 # 执行结束时间
testcase_testresult = 8 # 执行结果

#测试步骤表中部分列对应的数字序号(登陆和发邮件测试工作表)
teststep_teststepdescribe = 1 # 测试步骤描述

teststep_keywords = 2 #关键字
teststep_locationtype = 3 #定位方式
teststep_locatorexpression = 4 #定位操作属性值
teststep_operatevalue = 5 #操作值
teststep_runtime = 6 #测试时间
teststep_testresult = 7 #测试结果
teststep_errorinfo = 8 #错误信息
teststep_errorpic = 9 #错误截图

#数据源表中，是否执行列对应的数字编号(联系人)
datasource_isexecute = 6 #是否执行
datasource_email = 2 #电子邮箱
datasource_runtime = 7 #执行时间
datasource_result = 8 #执行结果
datasource_phone= 3 #手机号码













































