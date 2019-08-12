#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: get_word_with_baidu_name_top400.py
@time: 2019-7-27 8:42
@desc:
"""

name_top400_dict = []
with open('G:\\word_with_top_300_name_baidu_dict.txt', 'r', encoding='utf-8') as r:
    for item in r:
        name_top400_dict.append(item.strip())

with open('G:\\word_with_top_300_name.txt', 'r', encoding='utf-8') as f:
    with open('G:\\word_with_top_300_name_none_baidu_dict.txt', 'w', encoding='utf-8') as w:
        for item in f:
            if item.strip() not in name_top400_dict:
                print(item.strip())
                w.write(item.strip())
                w.write('\n')
                w.flush()