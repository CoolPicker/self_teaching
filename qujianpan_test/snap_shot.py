#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: snap_shot.py
@time: 2019-8-19 17:01
@desc:
"""

import cv2
import os

dirpath = 'C:\\Users\\nya\\Nox_share\\ImageShare\\res\\9-5\\'
respath = 'G:\\qujianpan\\9-5\\'
file_arr = os.listdir(dirpath)
for item in file_arr:
    filepath = dirpath + item
    image = cv2.imread(filepath)
    cropImg = image[750:830, 0:645]
    cv2.imwrite(respath + item, cropImg)
    print(respath+item)

