#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 17:25
# @Author  : logger

'''日志模块'''
import logging
import time
import os
import sys

class logger():
    def __init__(self):
        #创建一个logger
        self.logger = logging.getLogger()
        #定义log级别，定义debug后，所有类型都会打印
        self.logger.setLevel(logging.DEBUG)
        timetup = time.localtime()
        # 获取年月日
        currentdate = str(timetup.tm_year) + '-' + \
                      str(timetup.tm_mon) + '-' + str(timetup.tm_mday)
        log_names = '../log/'

        # #如果没有log目录，则创建
        # if not os.path.exists(log_names):os.makedirs(log_names)
        #防止请求重复的日志
        if not self.logger.handlers:
            #设置当前时间
            # rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #设置存放日志的名字
            log_name = log_names + currentdate + '.log'
            # if not os.path.exists(log_name): os.makedirs(log_name)
            ##向文件输出日志
            fh = logging.FileHandler(log_name,encoding='utf-8')
            #设置输出级别
            fh.setLevel(logging.DEBUG)



            #再设置输入到控制台，即屏幕
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)


            #定义输入日志的格式
            formafer = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

            #设置格式
            fh.setFormatter(formafer)
            # ch.setFormatter(formafer)

            # 给logger添加handler
            self.logger.addHandler(fh)
            # self.logger.addHandler(ch)


    def getlog(self):
         return self.logger
def write(message):
        messages = str(message)

        ct = time.time()
        local_time = time.localtime(ct)
        currentdate = str(local_time.tm_year) + '-' + \
                      str(local_time.tm_mon) + '-' + str(local_time.tm_mday)
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        data_secs = (ct - int(ct)) * 1000
        time_stamp = "%s.%03d" % (data_head, data_secs)
        log_names = '../log/'
        log_name = log_names+currentdate + '.log'
        try:
            log = open(log_name,'a')
            terminal = sys.stdout
            terminal.write(time_stamp+': '+messages)
            log.write(time_stamp+': '+messages+'\n')
        except Exception as e:
            raise e

if __name__=='__main__':
    logger = logger()
    logger.logger.error('djsoadja')
    logger.getlog()

