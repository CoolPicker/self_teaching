#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: get_first_column_word.py
@time: 2019-7-26 19:02
@desc:
"""

with open('G:\\ngram_lex_base_clean.txt', 'r', encoding='utf-8') as r:
    with open('G:\\ngram_only_word.txt', 'w', encoding='utf-8') as w:
        i = 1
        for item in r:
            print(str(i/672000))
            i = i + 1
            items = item.strip().split('\t')
            word = items[0]
            if len(word) > 1:
                w.write(word)
                w.write('\n')
                w.flush()