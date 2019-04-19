#!usr/bin/env python
# -*- coding:utf-8 -*-
import win32clipboard as w
import win32con

class clipboard(object):
    '''
    模拟Windows设置剪贴板
    '''
    #读取剪贴板
    @staticmethod
    def gettext():
        #打开剪贴板
        w.OpenClipboard()
        #获取剪贴板中的数据
        d = w.GetClipboardData(win32con.CF_TEXT)
        #关闭剪贴板
        w.CloseClipboard()
        #返回剪贴板数据给调用者
        return d
    #设置剪贴板内容
    @staticmethod
    def settext(asring):
        #打开剪贴板s
        w.OpenClipboard()
        #清空剪贴板s
        w.EmptyClipboard()
        #将数据astring写入剪贴板
        w.SetClipboardData(win32con.CF_UNICODETEXT,asring)
        #关闭剪贴板
        w.CloseClipboard()


if __name__=='__main__':
    from DataDrivenFrameWork.util.keyboardutil import keyboardkeys
    cli = clipboard()
    cli.settext(u'../a.txt')

    c = cli.gettext()
    print(type(c))
    keyboardkeys.towkeys("ctrl",'v')
    #模拟回车键，以便加载要上传的附件
    keyboardkeys.onekey("enter")
    print(c)

