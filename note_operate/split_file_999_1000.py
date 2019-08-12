#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: split_file_999_1000.py
@time: 2019-8-6 19:54
@desc:
"""
from pypinyin import lazy_pinyin


def file_charge(num):
    filename = str(num) + '.txt'
    req_arr = []
    with open('G:\\ngram_lexer\\sogou_input\\single-req\\' + filename, 'r', encoding='utf-8') as fr:
        for item in fr:
            req_arr.append(item.strip())
    res_arr = []
    with open('G:\\ngram_lexer\\sogou_input\\nn\\' + filename, 'r', encoding='utf-8') as fs:
        for item in fs:
            item = item.strip()
            pins = lazy_pinyin(item)
            res_arr.append(''.join(pins))

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
    print(str(num) + ' --- ' + str(now - 1))


file_charge(438)