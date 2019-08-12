#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: split_file_dump_check.py
@time: 2019-8-6 19:44
@desc:
"""

from pypinyin import lazy_pinyin

for i in range(401, 721):
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
                    pins = lazy_pinyin(item)
                    res_arr.append(''.join(pins))
        except:
            print(filename)

        # kk = 1
        # for i1, i2 in zip(req_arr, res_arr):
        #     if i1 != i2:
        #         kk = kk + 1
        # if kk > 50:
        #     print(filename)
        ee = 1
        heihei = 1
        hei_count = 0
        now = 1
        for i1, i2 in zip(req_arr, res_arr):
            if i1 != i2:
                if heihei == ee:
                    if hei_count == 0:
                        now = ee
                        hei_count = 1
                    elif hei_count < 5:
                        hei_count = hei_count + 1
                    else:
                        break
                else:
                    hei_count = 0
                heihei = ee + 1
            ee = ee + 1
        if hei_count == 5:
            print(filename + ' --- ' + str(now - 1))

