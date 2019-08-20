#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: test.py
@time: 2019-8-16 17:27
@desc:
"""
path = 'G:\\ngram_lexer\\sogou_input\\'
base_path = 'v2_clean_base.txt'
before_path = 'v2_clean_base_res.txt'
last_path = 'v2_clean_last.txt'
pin_freq = {}
pin_set = set()
with open(path+base_path, 'r', encoding='utf-8') as rb:
    for item in rb:
        items = item.strip().split('\t')
        word = items[0]
        pins = items[1]
        frequency = items[2]

        before_length = len(pin_set)
        pin_set.add(pins)
        after_length = len(pin_set)
        if after_length > before_length:
            pin_freq[pins] = frequency


print(len(pin_set))
with open(path+before_path, 'r', encoding='utf-8') as re:
    with open(path+last_path, 'w', encoding='utf-8') as w:
        for item in re:
            items = item.strip().split('\t')
            word = items[0]
            pins = items[1]
            frequency = pin_freq[pins]
            if frequency:
                w.write(word+'\t'+pins+'\t'+frequency)
                w.write('\n')
                w.flush()
            else:
                print(item)