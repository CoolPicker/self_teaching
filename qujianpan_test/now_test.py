#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: now_test.py
@time: 2019-8-19 15:31
@desc:
"""
position_dict_26 = {'q': '35, 901',
                    'w': '110, 903',
                    'e': '179, 900',
                    'r': '250, 900',
                    't': '323, 900',
                    'y': '394, 903',
                    'u': '469, 901',
                    'i': '539, 904',
                    'o': '619, 899',
                    'p': '682, 901',
                    'a': '65, 1011',
                    'l': '653, 1011',
                    's': '135, 1011',
                    'd': '212, 1011',
                    'f': '287, 1011',
                    'g': '358, 1011',
                    'h': '432, 1011',
                    'j': '507, 1011',
                    'k': '580, 1011',
                    'z': '137, 1118',
                    'x': '210, 1118',
                    'c': '285, 1118',
                    'v': '359, 1118',
                    'b': '432, 1118',
                    'n': '506, 1118',
                    'm': '578, 1118',
                    '0': '670, 1220'}
position_dict_9 = {'0': '669, 1222',
                   '2': '363, 902',
                   '3': '530, 902',
                   '4': '204, 1008',
                   '5': '363, 1008',
                   '6': '530, 1008',
                   '7': '204, 1119',
                   '8': '363, 1119',
                   '9': '530, 1119'}


with open('C:\\Users\\nya\\Nox_share\\ImageShare\\five_9.txt', 'r', encoding='utf-8') as r:
    with open('C:\\Users\\nya\\Nox_share\\ImageShare\\5-9.txt', 'w', encoding='utf-8') as w:
        for item in r:
            item = item.strip()
            for key in item:
                split_each = position_dict_9[key]
                eachs = split_each.strip().split(',')
                x = eachs[0].strip()
                y = eachs[1].strip()
                w.write('Tap ' + x + ', ' + y)
                w.write('\n')
                w.flush()
            w.write('Delay 1000')
            w.write('\n')
            w.write('SnapShot "/sdcard/Pictures/res/9-5/' + item + '.png"')
            w.write('\n')
            w.write('Tap 670, 1220')
            w.write('\n')
            w.write('Tap 670, 1220')
            w.write('\n')
            w.flush()


# with open('C:\\Users\\nya\\Nox_share\\ImageShare\\five_26.txt', 'r', encoding='utf-8') as r:
#     with open('C:\\Users\\nya\\Nox_share\\ImageShare\\26-5.txt', 'w', encoding='utf-8') as w:
#         for item in r:
#             item = item.strip()
#             for key in item:
#                 split_each = position_dict_26[key]
#                 eachs = split_each.strip().split(',')
#                 x = eachs[0].strip()
#                 y = eachs[1].strip()
#                 w.write('Tap ' + x + ', ' + y)
#                 w.write('\n')
#                 w.flush()
#             w.write('Delay 1000')
#             w.write('\n')
#             w.write('SnapShot "/sdcard/Pictures/res/26-5/' + item + '.png"')
#             w.write('\n')
#             w.write('Tap 670, 1220')
#             w.write('\n')
#             w.write('Tap 670, 1220')
#             w.write('\n')
#             w.flush()
