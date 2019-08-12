#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: ngram_base_sorted.py
@time: 2019-7-29 13:31
@desc:
"""


import operator

word_arr = []
with open('G:\\ngram_lexer\\sogou_input\\res.txt', 'r', encoding='utf-8') as f:
    for item in f:
        item_arr = item.strip().split('\t')
        word = item_arr[0].strip()
        encode_word = word.encode('utf-8')
        pypinyin = item_arr[1].strip()
        frequency = item_arr[2].strip()
        each = []
        each.append(word)
        each.append(pypinyin)
        each.append(frequency)
        each.append(-1 * int(frequency))
        # each.append(length)
        # each.append(encode_word)
        word_arr.append(each)

# word_arr.sort(key=operator.itemgetter(2))
# word_arr.sort(reverse=True)
word_arr.sort(key=operator.itemgetter(3))


with open('G:\\ngram_lexer\\sogou_input\\res_sorted.txt', 'w', encoding='utf-8') as w:
    i = 1
    for item in word_arr:
        i = i + 1
        now = item[0] + '\t' + item[1] + '\t' + item[2]
        w.write(now)
        w.write('\n')
        w.flush()

