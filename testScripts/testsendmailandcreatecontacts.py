#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 10:29
# @Author  : Aries
# @Site    : 
# @File    : testsendmailandcreatecontacts.py
# @Software: PyCharm
import traceback
from  DataDrivenFrameWork.testScripts.writetestresult import writetestresult
from DataDrivenFrameWork.testScripts import createcontacts
from DataDrivenFrameWork.action.pageaction import *
from DataDrivenFrameWork.config.varconfig import *
import unittest
import ddt
from Apitest.common import HTMLTestRunner_Chart

@ddt.ddt
class runtestcase(unittest.TestCase):
        @classmethod
        def setUp(cls):
            pass
        @classmethod
        def test_testsendmailandcreatecontacts(cls):
            try:
                #根据excel文件中的sheet名获取shee对象
                casesheet = excelobj.getSheetByname(u'测试用例')
                #获取测试用例总行数
                caserows = excelobj.getrownumber(casesheet)

                #获取测试用例表sheet中是否执行对象
                isexecutecolumn = excelobj.getColumn(casesheet,testcase_isexcute)

                #记录执行成功的测试用例个数
                successfulcase = 0
                #记录需要执行的用例个数
                requiredcase = 0
                for idx,i in enumerate(isexecutecolumn[1:]):
                    mylog.info('"%s %s"'%(idx,i))
                    #因为用例sheet的第一行为标题行，无须执行
                    casename = excelobj.getcellofvalue(casesheet,rowno=idx+2,colsno=testcase_testcasename)

                    #遍历测试用例表中执行被设置Y的用例
                    if i=='y':
                        mylog.debug(i)
                        requiredcase += 1
                        #获取测试用例表中，第idx+1行中，执行时所使用的框架类型
                        userframeworkname = excelobj.getcellofvalue(
                            casesheet,rowno=idx+2,colsno=testcase_frameworkname
                        )

                        #获取测试用例表中，第idx+1行中数据驱动 的数据源sheet名
                        stepsheetname = excelobj.getcellofvalue(
                            casesheet,rowno=idx+2,colsno=testcase_testsheetname
                        )
                        #如果框架类型为‘数据’
                        if userframeworkname == u'数据':
                            # mylog.info('----调用数据驱动-----')
                            #依次遍历获取用例步骤名称
                            datasheetname = excelobj.getcellofvalue(
                                casesheet,rowno = idx+2,
                                colsno=testcase_datasourcesheetname
                            )
                            #获取第idx+1测试用例的数据驱动的数据源sheet名[数据源工作表]
                            setpsheetobj = excelobj.getSheetByname(stepsheetname)

                            #获取第idx+1测试用例使用的数据sheet对象[步骤工作表]
                            datasheetobj = excelobj.getSheetByname(datasheetname)

                            #通过数据驱动框架执行添加联系人
                            result = createcontacts.datadriverfun(setpsheetobj,datasheetobj)
                            #如果为真
                            if result:
                                mylog.debug(u'用例 "%s" 执行成功' % casename)
                                successfulcase += 1
                                #想用例表中写入测试结果
                                writetestresult(casesheet,rowno=idx+2,colsno="testcase",
                                                testresult='pass')
                            else:
                                mylog.debug(u'用例 "%s" 执行失败' % casename)
                                writetestresult(casesheet, rowno=idx + 2, colsno="testcase",
                                                testresult='faild')

                        elif userframeworkname == u'关键字':
                            mylog.info('----调用关键字驱动-----')
                            #获取数据源名称
                            casestepobj = excelobj.getSheetByname(stepsheetname)
                            #获取总行数
                            stepnums = excelobj.getrownumber(casestepobj)
                            #记录成功数
                            successfulstep = 0
                            mylog.info(u'测试用例一共 %s 步' % stepnums)
                            #因为从第二行开始，所有总数要加一
                            for index in range(2,stepnums+1):
                                #获取步骤sheet中第index行对象，获取所有数据
                                steprow = excelobj.getrow(casestepobj,index)

                                #获取关键字作为调用的函数名，因为关函数名在第三列
                                # ，但是遍历从0开始，所以要减一
                                keyword = steprow[teststep_keywords-1]

                                #获取操作元素定位方式
                                locationtype = steprow[teststep_locationtype-1]

                                #获取定位方式的属性表达式
                                locationexpression = steprow[teststep_locatorexpression-1]

                                #获取操作值
                                operatevalue = steprow[teststep_operatevalue-1]

                                if isinstance(operatevalue,int):
                                    #如果操作值为数字型，将其转换字符串，方便拼接
                                    operatevalue = str(operatevalue)
                                #构造需要执行的表达式，该表达式对应封装文件的pageaction方法
                                tmpstr = "'%s','%s'" %(locationtype.lower(),#转换小写
                                                       locationexpression.replace("'",'"')#替换新值
                                                       ) if locationtype and locationexpression else ""
                                if tmpstr:
                                    #如果为真，拼接操作值字符串
                                    tmpstr +=\
                                        ",u'" + operatevalue+"'" if operatevalue else ''
                                else:
                                    tmpstr += \
                                        "u'" + operatevalue + "'" if operatevalue else ''
                                runstr = keyword + '('+tmpstr +')'
                                try:
                                    #     #通过eval函数，讲拼接的页面动作函数调用的字符串表示
                                    #     #当成有效的Python表达式执行，从而执行测试步骤的sheet中
                                    #     #关键字在ageaction.py文件中对应的映射方法,来完成页面元素的操作
                                        print(eval(runstr))
                                        cls.assertIn()
                                except Exception as e:
                                    mylog.info(u'执行步骤 “%s” 发生异常' \
                                          % steprow[teststep_teststepdescribe - 1],e)
                                    #截取异常屏幕图片
                                    capturepic = capture_screen()
                                    #获取详细的异常堆栈信息
                                    errorinfo = traceback.format_exc()
                                    #调用放大，传入参数
                                    writetestresult(casestepobj,rowno=index,
                                                    colsno='casestep',testresult='faild',
                                                    errorinfo=str(errorinfo),picpath=capturepic)
                                else:
                                    successfulstep += 1
                                    mylog.info(u'执行步骤 “%s” 成功' \
                                          % steprow[teststep_teststepdescribe - 1])
                                    writetestresult(casestepobj,rowno=index,colsno='casestep'
                                                        ,testresult='pass')

                            if successfulstep == stepnums - 1:
                                successfulcase += 1
                                # 如果成功执行的数量等于步骤中给出的步骤数
                                # 说明第idx+2行的数据执行通过，写入通过信息
                                mylog.info(u"用例 ’%s‘ 执行通过" % casename)
                                writetestresult(casesheet,
                                                rowno=idx + 2, colsno='testcase',
                                                testresult='pass')
                            else:
                                # 写入失败信息
                                mylog.info(u"用例 ’%s‘ 执行失败" % casename)
                                writetestresult(casesheet,
                                                rowno=idx + 2, colsno='testcase',
                                                testresult='faild')
                    else:
                        try:
                            # 将不需要的数据的执行时间和结果单元格清空
                            writetestresult(casename,
                                            rowno=idx + 2, colsno='testcase',
                                            testresult='')
                        except Exception as e:
                            pass
                            mylog.debug(e)

                    mylog.info(u'共 "%d" 条用例，"%d" 条需要被执行，成功执行 "%d 条"'\
                          % (caserows-1,requiredcase,successfulcase))

            except Exception as e:
                if e is not None:
                    mylog.warning(e)



def add_case(rule="testsendmailand*.py"):
    try:

        '''加载所有的测试用例'''
        datapath = os.path.join(parentdifpath,'testScripts')
        print(datapath)
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