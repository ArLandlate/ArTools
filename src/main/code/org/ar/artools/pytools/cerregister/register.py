#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time
import _thread
import argparse
from pykeyboard import *

# 接收外部传参
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("--alias", type=str, default="maven00")
parser.add_argument("--filepath", type=str, default="D:/ArSpace/Development/Java/cer/repo-maven-apache-org.cer")
args = parser.parse_args()  

alias = args.alias
filepath = args.filepath

batpath = os.path.abspath('.') + "/keytool.bat"

# 线程执行bat
def batstart():
    os.system(batpath + " " + alias + " " + filepath)

_thread.start_new_thread ( batstart, () )

time.sleep(2)

# 操作键盘输入密码和确认

k = PyKeyboard()

#k.tap_key('a')
k.type_string("changeit")

time.sleep(1)
k.tap_key(k.enter_key)

time.sleep(1)
k.type_string("changeit")

time.sleep(1)
k.tap_key(k.enter_key)

time.sleep(1)
k.type_string("Y")

time.sleep(1)
k.tap_key(k.enter_key)