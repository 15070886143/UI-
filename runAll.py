#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 14:18
# @Author  : runAll
# coding=utf-8
import unittest
from Apitest.common import HTMLTestRunner_Chart
from DataDrivenFrameWork.action.pageaction import *
from DataDrivenFrameWork.config.varconfig import *
def add_case(rule="testsendmailwith*.py"):
    try:
        '''加载所有的测试用例'''
        datapath = os.path.join(parentdifpath,'testScripts')
        # 定义discover方法的参数
        discover = unittest.defaultTestLoader.discover(datapath,
                                                  pattern=rule,)
        return discover
    except Exception as e:
        raise e

def run_case(all_case):
    try:
        '''执行所有的用例, 并把结果写入测试报告'''
        report_path = os.path.join(parentdifpath, "report")
        # 如果不存在该目录，则创建
        if not os.path.exists(report_path): os.mkdir(report_path)
        htmlreport = report_path + r"\result.html"
        # xlsxreport = reportpath+r"\result.xlsx"
        print("测试报告生成地址：%s" % htmlreport)
        fp = open(htmlreport, "wb")
        runner = HTMLTestRunner_Chart.HTMLTestRunner(
            stream=fp,
            title=u'自动化测试报告',
            description='详细测试用例结果',
        )
        # 调用add_case函数返回值
        runner.run(all_case)
        # readmail.sendMail(htmlreport,xlsxreport)
        fp.close()
    except Exception as e:
        raise e

if __name__ == '__main__':
    # 获取当前的report目
    cases = add_case()
    run_case(cases)




