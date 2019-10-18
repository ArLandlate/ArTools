#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
author: ArLandlate
function: listen keyboard events and cut down the full screenshot and save
"""

import time
import os
import imageUtil
import sys

sys.path.append("../util")
import commonUtil

def cutshot():
    """
    cut down current full screenshot and save
    :return: image name if success
    """
    # 使用日期时间作为图片名
    imgpath = os.path.abspath('../../../../../../resources/screenshots/pictures/')
    imgname = time.strftime("%Y-%m-%d %H%M%S", time.localtime())
    imgextension = ".png"

    imgaddr = imgpath + imgname
    imgaddr_origin = imgaddr

    if not os.path.isdir(imgpath):  # 无文件夹时创建
        os.makedirs(imgpath)

    # 重名校验
    no = 2
    while os.path.isfile(imgaddr + imgextension):
        imgaddr = imgaddr_origin + "(" + str(no) + ")"
        no += 1

    imgaddr += imgextension

    if imageUtil.getFullScreenShot(imgaddr):
        return imgaddr

def keyboardListener(event):
    """
    method for keyboard
    """
    if event.ScanCode == 55:
        ret = cutshot()
        if ret:
            print("cut down success: \n\t" + ret)

    return True

"""
Main
"""
commonUtil.hookPump(keyboardListener)
