#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: test_count.py
@time: 2019-8-3 10:41
@desc:
"""

pin_set = set()

with open('G:\\ngram_lexer\\new\\word_6w3.txt', 'r', encoding='utf-8') as r:
    for item in r:
        pin_set.add(item.strip())

print(len(pin_set))
with open('G:\\ngram_lexer\\new\\res_63.txt', 'r', encoding='utf-8') as r:
    for item in r:
        items = item.strip().split('\t')
        pinyin = items[0]
        if pinyin in pin_set:
            pin_set.remove(pinyin)
        else:
            print(pinyin)