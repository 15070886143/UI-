#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 14:27
# @Author  : Aries
# @Site    : 
# @File    : dirandtime.py
# @Software: PyCharm
import time,os
from datetime import datetime
from DataDrivenFrameWork.config.varconfig import screenpicyuresdir
#获取当前日期
def getcurrentdate():
    #获取所有日期
    timetup = time.localtime()
    #获取年月日
    currentdate = str(timetup.tm_year) + '-'+\
        str(timetup.tm_mon) + '-' + str(timetup.tm_mday)
    return currentdate


#获取当前时间
def getcurrenttime():
    #获取当前日期和时间
    timestr = datetime.now()
    #取时分秒和毫秒
    nowtime = timestr.strftime('%H-%M-%S-%f')
    return  nowtime

#获取当前年月日加时
def getcurrenttimes():
    times =  time.strftime('%Y%m%d%H', time.localtime(time.time()))
    return times
#创建截图存放的目录
def createcurrentdatedir():
    #创建截图目录名称为时间格式
    dirname = os.path.join(screenpicyuresdir,getcurrentdate())
    #判断是否存在目录，不存在则创建
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    return dirname

# 清除浏览器cookies



