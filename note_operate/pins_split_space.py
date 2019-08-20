#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: pins_split_space.py
@time: 2019-8-13 9:47
@desc:
"""

pin_dict = {}
with open('G:\\ngram_lexer\\sogou_input\\ngram_20w_others_single.txt', 'r', encoding='utf-8') as f:
    for item in f:
        item = item.strip()
        key = ''.join(item.split(' '))
        if key not in pin_dict.keys():
            pin_dict[key] = item
        else:
            continue
with open('G:\\ngram_lexer\\sogou_input\\single_res_1501_2505.txt', 'r', encoding='utf-8') as r:
    with open('G:\\ngram_lexer\\sogou_input\\res_1501_2505.txt', 'w', encoding='utf-8') as w:
        for item in r:
            items = item.strip().split('\t')
            word = items[0].strip()
            key = items[1].strip()
            value = pin_dict[key]
            w.write(word + '\t' + value)
            w.write('\n')
            w.flush()
