#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: add_word_count.py
@time: 2019-7-17 18:09
@desc:
"""

with open('G:\\11.txt', 'r', encoding='utf-8') as r:
    with open('G:\\base_dict_20w_0712.txt', 'r', encoding='utf-8') as rf:
        with open('G:\\res.txt', 'w', encoding='utf-8') as w:
            with open('G:\\none.txt', 'w', encoding='utf-8') as wn:
                now_dict = {}
                for item in r:
                    items = item.strip().split('\t')
                    key = items[0] + '-' + items[1]
                    value = items[2]
                    now_dict[key] = value
                for each in rf:
                    eachs = each.strip().split('\t')
                    key_now = eachs[0] + '-' + eachs[1]
                    if key_now in now_dict.keys():
                        count = now_dict[key_now]
                        w.write(eachs[0] + '\t' + eachs[1] + '\t' + count)
                        w.write('\n')
                        w.flush()
                    else:
                        wn.write(eachs[0] + '\t' + eachs[1])
                        wn.write('\n')
                        wn.flush()
