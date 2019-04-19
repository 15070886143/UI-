#!usr/bin/env python
# -*- coding:utf-8 -*-
from . import *
from DataDrivenFrameWork.config.varconfig import *
from DataDrivenFrameWork.util.readExcel import *
import traceback
from DataDrivenFrameWork.config.varconfig import mylog
#用例结束后，想Excel写入执行结果信息
def writetestresult(sheetobj,rowno,colsno,testresult,errorinfo= None,picpath= None):
    mylog.debug(sheetobj,rowno,colsno,testresult,errorinfo,picpath)
    #测试通过绿色，失败红色
    colordic = {'pass':'green','faild':'red','':None}
    #对应执行时间和执行 结果，因为测试用例和用例步骤表中国都有执
    # 行时间和直接结果一列，定义此字典对象是为了区分应该写入哪个工作表
    colsdict= {
        'testcase':[testcase_runtime,testcase_testresult],
        'casestep':[teststep_runtime,teststep_testresult],
        'datasheet':[datasource_runtime,datasource_result]
    }
    try:
        # 在测试步骤的sheet表中，写入测试结果
        #被调用时，传入的参数一一对应，如，在testsendmailandcreatecontacts方法中
        # ，成功时写入的参数colsno='casestep',testresult='faild',就是把上面的参数传
        # 入到下面的writecell方法中，写入到文件
        excelobj.writecell(sheetobj,content = testresult,
                           rowno = rowno,colsno=colsdict[colsno][1],
                           style=colordic[testresult])
        if testresult =='':
            #清空时间单元格内容
            excelobj.writecell(sheetobj,content='',rowno = rowno,
                               colsno= colsdict[colsno][0])
        else:
            #在测试步骤sheet中，写入测试时间
            excelobj.writecellcurrenttime(sheetobj,rowno= rowno,
                                          colsno=colsdict[colsno][0])
        if  errorinfo and picpath:
            #在测试步骤sheet中，写入异常信息
            excelobj.writecell(sheetobj,content=errorinfo,rowno=rowno,colsno=teststep_errorinfo)
            #写入异常截图路径
            excelobj.writecell(sheetobj,content=picpath,rowno=rowno,colsno=teststep_errorpic)
        else:
            if colsno =='casestep':
                # 在测试步骤表中，清空异常信息单元格
                excelobj.writecell(sheetobj,content='',rowno=rowno,colsno=teststep_errorinfo)
                #在测试步骤表中，清空异常信息单元格
                excelobj.writecell(sheetobj,content='',rowno=rowno,colsno=teststep_errorpic)

    except Exception as e:
        mylog.error(e,u'写入Excel时发生异常')
        print(traceback.print_exc())


# 注释：该方法用于实现向Excel中 写入测试结果信息的公共方法