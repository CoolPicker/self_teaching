#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: replace_column.py
@time: 2019-7-15 10:25
@desc:
"""


for i in range(1, 6):
    with open('G:\\语言模型生成\\octopus\\test_cases\\sogou\\sogou' + str(i) + '.txt', 'r', encoding='utf-8') as f:
        with open('G:\\语言模型生成\\octopus\\test_cases\\sogou\\test' + str(i) + '.txt', 'w', encoding='utf-8') as w:
            for item in f:
                items = item.strip().split('\t')
                then = items[1] + '\t' + items[0]
                w.write(then)
                w.write('\n')
                w.flush()

