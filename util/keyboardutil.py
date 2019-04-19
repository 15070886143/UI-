#!usr/bin/env python
# -*- coding:utf-8 -*-
import win32api
import win32con

class keyboardkeys(object):
    '''
    模拟键盘按键类
    '''
    #创建回车，Ctrl和V键key值
    vk_code = {
        'enter':0x0D,
        'ctrl':0x11,
        'v':0x56
    }
    #该方法不强制要求传递参数，如下声明一个静态方法：
    @staticmethod
      # win32api.keybd_event有四个参数
      # 第一个为按键的虚拟键值，如回车键为vk_return, tab键为vk_tab（其他具体的参见附录：常用模拟键的键值对照表）；
      #
      # 第二个参数为扫描码，一般不用设置，用0代替就行；
      #
      # 第三个参数为选项标志，如果为keydown则置0即可，如果为keyup则设成"KEYEVENTF_KEYUP"；
      #
      # 第四个参数一般也是置0即可。
    def keydown(keyname):
        #按下按键
        win32api.keybd_event(keyboardkeys.vk_code[keyname],0,0,0)
    @staticmethod
    def keyup(keyname):
         #释放按键
        win32api.keybd_event(keyboardkeys.vk_code[keyname],0,win32con.KEYEVENTF_KEYUP,0)
    @staticmethod
    def onekey(key):
        #模拟单个按键
        keyboardkeys.keydown(key)
        keyboardkeys.keyup(key)
    @staticmethod
    def towkeys(key1,key2):
        #模拟多个组合键
        keyboardkeys.keydown(key1)
        keyboardkeys.keydown(key2)
        keyboardkeys.keyup(key1)
        keyboardkeys.keyup(key2)

