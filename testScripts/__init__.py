#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DataDrivenFrameWork.action.pageaction import *
from DataDrivenFrameWork.util.readExcel import ParseExcel
from DataDrivenFrameWork.config.varconfig import *
import time
import traceback
#设置编码为utf-8
#

#创建Excel解析对象

excelobj = ParseExcel()

#讲Excel数据文件加载到内存

excelobj.loadWoekBook(datafilepath)

