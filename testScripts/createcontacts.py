#!usr/bin/env python
# -*- coding:utf-8 -*-
from . import *
from DataDrivenFrameWork.testScripts.writetestresult import writetestresult
from DataDrivenFrameWork.config.varconfig import *
import traceback
from DataDrivenFrameWork.config.varconfig import mylog

def datadriverfun(datasourcesheetobj,stepsheetobj):
    mylog.info(datasourcesheetobj,stepsheetobj)
    try:
        #获取数据源表中的是否执行列对象,第六行‘是否执行’
        dataisexecutecolumn = excelobj.getColumn(
            datasourcesheetobj,
            datasource_isexecute
        )

        #获取数据源表中电子邮箱列对象
        emailcolumn = excelobj.getColumn(
            datasourcesheetobj,datasource_email
        )
        #获取测试步骤表中存在数据区域的行数
        setprownums = excelobj.getrownumber(stepsheetobj)
        #记录成功执行的数据条数
        successdatas= 0
        #记录被是设置为执行的数据条数
        requiredatas = 0
        #从dataisexecutecolumn第二个参数开始
        for idx,data in enumerate(dataisexecutecolumn[1:]):
            mylog.info("%s %s" % (idx,data))
            #遍历数据源表，准备进行数据驱动测试
            #因为第一行是标题行，所以从第二行开始遍历
            # 如果该列为y，执行
            if data =='y':
                #每遍历一次，行+1
                mylog.info(u"开始添加联系人 '%s'" % emailcolumn[idx + 1])
                requiredatas += 1
                #定义记录执行成功步骤变数量
                successstep = 0
                for index in range(2,setprownums + 1):
                    mylog.info(index)

                    #遍历添加联系人步骤表中所有的关键字数据
                    rowobj = excelobj.getrow(stepsheetobj,index)

                    #获取操作元素定位方式
                    locationtype = rowobj[teststep_locationtype - 1]

                    # 获取关键字
                    keyword = rowobj[teststep_keywords - 1]

                    #获取定位方式的属性表达式
                    locatorexpression = rowobj[teststep_locatorexpression - 1]

                    #获取操作值
                    operatevalue = rowobj[teststep_operatevalue -1]

                    #检查整型，转化为字符串
                    if isinstance(operatevalue,int):
                        operatevalue = str(operatevalue)

                    # isalpha()方法检测字符串是否只由字母组成。
                    if operatevalue and operatevalue.isalpha():
                        coordinate = operatevalue + str(idx +2)
                        print(coordinate,'coordinate')
                        #从联系人表中去查找对应列的数据coordinate为列序号
                        operatevalue = excelobj.getcellofvalue(
                            datasourcesheetobj,
                            coordinate=coordinate
                        )
                    tmpstr = "'%s','%s'" % (locationtype.lower(),  # 转换小写
                                            locatorexpression.replace("'", '"')  # 替换新值
                                            ) if locationtype and locatorexpression else ""

                    if isinstance(operatevalue,int):
                        operatevalue = str(operatevalue)

                    if tmpstr:
                        # 如果为真，拼接操作值字符串
                        tmpstr += \
                            ",u'" + operatevalue + "'" if operatevalue else ''
                    else:
                        tmpstr += \
                            "u'" + operatevalue + "'" if operatevalue else ''
                    runstr = keyword + '(' + tmpstr + ')'
                    mylog.debug(runstr)
                    try:
                        #     #通过eval函数，讲拼接的页面动作函数调用的字符串表示
                        #     #当成有效的Python表达式执行，从而执行测试步骤的sheet中
                        #     #关键字在ageaction.py文件中对应的映射方法,来完成页面元素的操作
                        eval(runstr)
                    except Exception as e:
                        mylog.debug(u'执行步骤 “%s” 发生异常'\
                              % rowobj[teststep_teststepdescribe-1],e)
                        # 截取异常屏幕图片
                        capturepic = capture_screen()
                        # 获取详细的异常堆栈信息
                        errorinfo = traceback.format_exc()
                        # 调用写入方法，当发生异常时，想工作表中写入数据，截图，异常错误等
                        writetestresult(sheetobj=stepsheetobj,
                                        rowno=index, colsno='casestep',
                                        testresult='faild',errorinfo=str(errorinfo),
                                        picpath=capturepic)
                    else:
                        successstep +=1
                        mylog.debug(u'执行步骤 “%s” 成功' \
                              %rowobj[teststep_teststepdescribe-1])
                        writetestresult(sheetobj=stepsheetobj,
                                        rowno=index, colsno='casestep',
                                        testresult='pass')
                # 如果执行步骤数=当前执行数
                mylog.info(setprownums,'setprownums数量','-----',successstep+1,'successstep数量')
                if setprownums == successstep+1:

                    #执行成功数+1
                    successdatas +=1
                    #再向表中写入数据“pass"
                    writetestresult(sheetobj = datasourcesheetobj,
                                    rowno=idx+2,colsno='datasheet',
                                    testresult='pass')

                else:
                    #写入失败信息
                    writetestresult(sheetobj=datasourcesheetobj,
                                    rowno=idx + 2, colsno='datasheet',
                                    testresult='faild')

            else:
                #将不需要的数据的执行时间和结果单元格清空
                writetestresult(sheetobj=datasourcesheetobj,
                                rowno=idx + 2, colsno='datasheet',
                                testresult='')
                writetestresult(sheetobj=stepsheetobj,
                                rowno=idx + 2, colsno='casestep',
                                testresult='')
        #当执行完成之后，如果执行成功数等于需要被执行数时，把值返回，
        # 供testsendmailandcreatecontacts文件中的数据驱动调用
        if requiredatas == successdatas:
            return 1
        return 0

    except Exception as e:
        raise e
#注释：用于实现向邮箱添加联系人的数据驱动框架部分

