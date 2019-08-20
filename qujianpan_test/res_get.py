#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: res_get.py
@time: 2019-8-20 10:37
@desc:
"""
each_dict = {}
with open('G:\\qujianpan\\9-5.txt', 'r', encoding='utf-8') as r:
    for item in r:
        items = item.strip().split('\t')
        each_dict[items[0]] = items[1]

with open('G:\\qujianpan\\req\\five_9.txt', 'r', encoding='utf-8') as f:
    with open('G:\\qujianpan\\res\\9-5.txt', 'w', encoding='utf-8') as w:
        for item in f:
            item = item.strip()
            value = each_dict[item]
            each = '\t'.join(value.split(' '))
            w.write(each)
            w.write('\n')
            w.flush()
