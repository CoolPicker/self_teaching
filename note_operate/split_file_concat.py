#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: split_file_concat.py
@time: 2019-8-6 20:39
@desc:
"""
total_arr = []
for i in range(1501, 2506):
    if i > 0:
        kk = 1
        filename = str(i) + '.txt'
        req_arr = []
        with open('G:\\ngram_lexer\\sogou_input\\single-req\\' + filename, 'r', encoding='utf-8') as fr:
            for item in fr:
                req_arr.append(item.strip())
        res_arr = []
        try:
            with open('G:\\ngram_lexer\\sogou_input\\nn\\' + filename, 'r', encoding='utf-8') as fs:
                for item in fs:
                    item = item.strip()
                    res_arr.append(item)
        except:
            print(filename)

        for i1, i2 in zip(req_arr, res_arr):
            total_arr.append(i2.strip() + '\t' + i1.strip())


print(len(total_arr))
with open('G:\\ngram_lexer\\sogou_input\\single_res_1501_2505.txt', 'w', encoding='utf-8') as w:
    for item in total_arr:
        w.write(item.strip())
        w.write('\n')
        w.flush()