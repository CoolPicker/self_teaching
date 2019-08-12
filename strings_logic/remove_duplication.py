#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: remove_duplication.py
@time: 2019-7-31 14:50
@desc:
"""
item_dict = {}
with open('G:\\ngram_lexer\\ttt.txt', 'r', encoding='utf-8') as f:
    for item in f:
        item = item.strip()
        word = item.split('\t')[0]
        item_dict[word] = item

with open('G:\\ngram_lexer\\res_lexer_rmdup.txt', 'r', encoding='utf-8') as r:
    with open('G:\\ngram_lexer\\res_lexer_0731.txt', 'w', encoding='utf-8') as w:
        for item in r:
            items = item.strip().split('\t')
            word = items[0]
            if word in item_dict.keys():
                w.write(item[word])
                w.write('\n')
                w.flush()
            else:
                w.write(item.strip())
                w.write('\n')
                w.flush()
# word_set = set()
# with open('G:\\ngram_lexer\\res_lexer.txt', 'r', encoding='utf-8') as f:
#     with open('G:\\ngram_lexer\\res_lexer_rmdup.txt', 'w', encoding='utf-8') as w:
#         for item in f:
#             size_before = len(word_set)
#             items = item.strip().split('\t')
#             word = items[0]
#             word_set.add(word)
#             size_after = len(word_set)
#             if size_after > size_before:
#                 w.write(item.strip())
#                 w.write('\n')
#                 w.flush()
