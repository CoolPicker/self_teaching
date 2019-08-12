#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: split_file.py
@time: 2019-8-6 19:39
@desc:
"""

ngram_set = set()
each = 1000
count = 0
for i in range(2306):
    if i > 525:
        index = 1
        with open('G:\\ngram_lexer\\sogou_input\\ngram_20w_others_single.txt', 'r', encoding='utf-8') as r:
            with open('G:\\ngram_lexer\\sogou_input\\single-req\\' + str(i + 200) + '.txt', 'w', encoding='utf-8') as w:
                for item in r:
                    if (i - 1) * each < index <= i * each:
                        item = item.strip()
                        pins = item.split(' ')
                        w.write(''.join(pins))
                        w.write('\n')
                        w.flush()
                    index = index + 1