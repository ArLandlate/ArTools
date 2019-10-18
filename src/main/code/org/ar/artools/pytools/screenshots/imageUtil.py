#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
author: ArLandlate
function: image util
"""

# import sys
# sys.path.append("../util")

from PIL import ImageGrab

# import commonUtil

def getFullScreenShot(path):
    # 抓取屏幕截图
    debug = False
    # img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
    img = ImageGrab.grab()

    if img:
        img.save(path)
        return True
