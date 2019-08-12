#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: enex_operate.py
@time: 2019-8-6 19:04
@desc:
"""

with open('G:\\ngram_lexer\\sogou_input\\301-400.enex', 'r', encoding='utf-8') as r:
    for item in r:
        each_arr = []
        item = item.strip()
        first_items = item.split('</title><div>')
        filename = str(first_items[0]) + '.txt'
        second_items = first_items[1].split('</div><div>')
        for each in second_items:
            each = each.strip()
            thirds = each.split('</div>')
            now = thirds[0].strip()
            each_arr.append(now)
        print(filename + '\t' + str(len(each_arr)))
        with open('G:\\ngram_lexer\\sogou_input\\nn\\' + filename, 'w', encoding='utf-8') as w:
            for ii in each_arr:
                ii = ii.strip()
                w.write(ii)
                w.write('\n')
                w.flush()