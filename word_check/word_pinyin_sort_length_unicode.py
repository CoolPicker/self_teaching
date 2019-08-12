#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

import operator

word_arr = []
with open('G:\\base_dict_20w_res_1.txt', 'r', encoding='utf-8') as f:
    for item in f:
        item_arr = item.strip().split('\t')
        word = item_arr[0]
        encode_word = word.encode('utf-8')
        pypinyin = item_arr[1]
        length = len(word)
        each = []
        each.append(word)
        each.append(pypinyin)
        each.append(length)
        each.append(encode_word)
        word_arr.append(each)


word_arr.sort(key=operator.itemgetter(2, 3))


with open('G:\\base_dict_20w_res_2.txt', 'w', encoding='utf-8') as w:
    for item in word_arr:
        now = item[0] + '\t' + item[1]
        w.write(now)
        w.write('\n')
        w.flush()

