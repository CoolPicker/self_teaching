#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: res_test.py
@time: 2019-8-1 10:05
@desc:
"""
from pypinyin import lazy_pinyin
# ngram_set = set()
# each = 1000
# count = 0
# for i in range(201):
#     if i > 0:
#         index = 1
#         with open('G:\\ngram_lexer\\sogou_input\\ngram_20w.txt', 'r', encoding='utf-8') as r:
#             with open('G:\\ngram_lexer\\sogou_input\\req\\' + str(i) + '.txt', 'w', encoding='utf-8') as w:
#                 for item in r:
#                     if (i - 1) * each < index <= i * each:
#                         items = item.strip().split('\t')
#                         pins = items[1].split(' ')
#                         cou = items[2]
#                         w.write(''.join(pins) + '\t' + cou)
#                         w.write('\n')
#                         w.flush()
#                     index = index + 1

for i in range(201):
    if i > 0:
        kk = 1
        filename = str(i) + '.txt'
        req_arr = []
        with open('G:\\ngram_lexer\\sogou_input\\req\\' + filename, 'r', encoding='utf-8') as fr:
            for item in fr:
                items = item.strip().split('\t')
                # req_arr.append(items[0])
                req_arr.append(item.strip())
        res_arr = []
        try:
            with open('G:\\ngram_lexer\\sogou_input\\res\\' + filename, 'r', encoding='utf-8') as fs:
                for item in fs:
                    item = item.strip()
                    pins = lazy_pinyin(item)
                    res_arr.append(item)
                    # res_arr.append(''.join(pins))
        except:
            print(filename)

        with open('G:\\ngram_lexer\\sogou_input\\gogo\\' + filename, 'w', encoding='utf-8') as w:
            for res1, res2 in zip(req_arr, res_arr):
                w.write(res2.strip() + '\t' + res1.strip())
                w.write('\n')
                w.flush()

        # for i1, i2 in zip(req_arr, res_arr):
        #     pass

# def file_charge(num):
#     filename = str(num) + '.txt'
#     req_arr = []
#     with open('G:\\ngram_lexer\\sogou_input\\req\\' + filename, 'r', encoding='utf-8') as fr:
#         for item in fr:
#             items = item.strip().split('\t')
#             req_arr.append(items[0])
#     res_arr = []
#     with open('G:\\ngram_lexer\\sogou_input\\res\\' + filename, 'r', encoding='utf-8') as fs:
#         for item in fs:
#             item = item.strip()
#             pins = lazy_pinyin(item)
#             res_arr.append(''.join(pins))
#
#     ee = 1
#     for i1, i2 in zip(req_arr, res_arr):
#         if i1 != i2:
#             print(ee)
#         ee = ee + 1
#
#
# file_charge(172)

