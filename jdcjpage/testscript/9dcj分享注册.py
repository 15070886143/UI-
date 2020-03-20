#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 16:06
# @Author  : Aries
# @Site    : 
# @File    : 9dcj分享注册.py
from DataDrivenFrameWork.jdcjpage.testsendmailwithattachment import *

if __name__ == '__main__':
    PC_url = 'https://www.9dcj.com.cn/7975?pfsntype=room_share&share_userid=88879#0-sqq-1-38759-9737f6f9e09dfaf5d3fd14d775bfee85'
    WAP_url = 'https://wap.9dcj.com/Zhiboinner/15496?pfsntype=room_share&share_userid=233858'
    weixin_uri = 'http://wap.9dcj.com/Zhiboinner/4398?pfsntype=room_share&share_userid=103706&sharetype=0-wexin-1'
    QQ_url = 'http://wap.9dcj.com/Zhiboinner/4398?pfsntype=room_share&share_userid=103706&sharetype=0-sqq-1'
    list_url = [PC_url, weixin_uri, QQ_url]
    share = share()
    share.setUp()
    #参数详解：第一位（要执行的次数），第二位（链接地址）
    #PC单个链接测试
    share.test_PC(2,PC_url)
    #wap单个链接测试
    # share.test_wap(2,WAP_url)
    #PC和wap一起测试
    # share.test_wpcs(4,5,list_url)
