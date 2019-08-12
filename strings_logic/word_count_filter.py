#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: word_count_filter.py
@time: 2019-7-29 14:08
@desc:
"""

with open("G:\\ngram_lexer\\v2_clean_base.txt", 'r', encoding='utf-8') as f:
    with open("G:\\ngram_lexer\\v2_clean_base_2_3_4.txt", 'w', encoding='utf-8') as w:
        i = 1
        for item in f:
            print(str(i / 3167123))
            i = i + 1
            items = item.strip().split('\t')
            now = items[0].strip()
            if 1 < len(now) < 5:
                w.write(now)
                w.write('\n')
                w.flush()

