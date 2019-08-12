#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

import operator

word_arr = []
with open('G:\\sougou_5k_py.txt', 'r', encoding='utf-8') as f:
    for item in f:
        item_arr = item.strip().split('\t')
        word = item_arr[0]
        pypinyin = item_arr[1]
        length = item_arr[2]
        source = item_arr[3]
        each = []
        each.append(word)
        each.append(pypinyin)
        each.append(length)
        each.append(source)
        word_arr.append(each)


word_arr.sort(key=operator.itemgetter(2,1))


with open('G:\\sougou_5k_test.txt', 'w', encoding='utf-8') as w:
    for item in word_arr:
        now = item[0] + '\t' + item[1] + '\t' + item[2] + '\t' + item[3]
        w.write(now)
        w.write('\n')
        w.flush()