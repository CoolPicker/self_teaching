#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: remove_repetition.py
@time: 2019-8-14 9:29
@desc:
"""

test_set = set()
with open('G:\\ngram_lexer\\sogou_input\\res_1501_2505.txt', 'r', encoding='utf-8') as f:
    with open('G:\\ngram_lexer\\sogou_input\\res_then_100w.txt', 'w', encoding='utf-8') as w:
        for item in f:
            items = item.strip().split('\t')
            before = test_set.__len__()
            test_set.add(items[0].strip())
            after = test_set.__len__()
            if after > before:
                w.write(item.strip())
                w.write('\n')
                w.flush()

