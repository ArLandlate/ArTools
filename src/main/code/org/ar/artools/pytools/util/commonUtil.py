#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
author: ArLandlate
function: common functions util
"""

import os
import win32api
import win32con
import time
import pythoncom
import PyHook3

def create_file(filename):
    """
    创建日志文件夹和日志文件
    :param filename: 文件全路径名
    :return: 文件流
    """
    path = filename[0:filename.rfind("/")]
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        return fd
    else:
        pass

def hookPump(eventsMethod):
    """
    监控键盘输入
    :param eventsMethod: 监听到键盘事件后执行的方法
    :return: None
    """
    #创建hook句柄
    hm = PyHook3.HookManager()
    #监控键盘
    hm.KeyDown = eventsMethod
    hm.HookKeyboard()
    #循环获取消息
    pythoncom.PumpMessages()
