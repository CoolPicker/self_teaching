#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

"""
排序 sort
"""

import operator

triplePath = 'G:\\triple.txt'

triple_arr = []
with open(triplePath, 'r', encoding='utf-8') as f:
    for item in f:
        item_arr = item.strip().split('\t')
        word = item_arr[0]
        pypinyin = item_arr[1]
        each = []
        each.append(word)
        each.append(pypinyin)
        each.append(len(word))
        triple_arr.append(each)


triple_arr.sort(key=operator.itemgetter(2,1))

index = 7524
with open('G:\\resTriple.txt', 'w', encoding='utf-8') as w:
    for item in triple_arr:
        now = str(index) + '\t' + item[0] + '\t' + item[1]
        index = index + 1
        w.write(now)
        w.write('\n')
        w.flush()