#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: data_file_iterator.py
@time: 2019-8-12 9:24
@desc:
"""
import os


def get_file_last_line(inputfile):
    filesize = os.path.getsize(inputfile)
    blocksize = 1024
    with open(inputfile, 'rb') as f:
        last_line = ""
        if filesize > blocksize:
            maxseekpoint = (filesize // blocksize)
            f.seek((maxseekpoint - 1) * blocksize)
        elif filesize:
            f.seek(0, 0)
        lines = f.readlines()
        if lines:
            lineno = 1
            while last_line == "":
                last_line = lines[-lineno].strip()
                lineno += 1
        return last_line


operate_file = 'G:\\ngram_lexer\\sogou_input\\' + '501-720.txt'
last_line = get_file_last_line(operate_file).decode('utf-8')
res_dict = {}
arr_each = []
now_key = ''
with open(operate_file, 'r', encoding='utf-8') as r:
    for item in r:
        item = item.strip()
        if item:
            if item.isdecimal():
                if arr_each:
                    res_dict[now_key] = arr_each
                    print('key end : ', now_key)
                now_key = item
                arr_each = []
                print('key start : ', now_key)
            elif item == last_line:
                res_dict[now_key] = arr_each
                print('key end : ', now_key)
            else:
                arr_each.append(item)


for key in res_dict.keys():
    print(key)
    now_use = res_dict[key]
    filename = key + '.txt'
    with open('G:\\ngram_lexer\\sogou_input\\nn\\' + filename, 'w', encoding='utf-8') as w:
        for ii in now_use:
            ii = ii.strip()
            w.write(ii)
            w.write('\n')
            w.flush()

