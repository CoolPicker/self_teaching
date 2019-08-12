#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

base_set = set()

with open('G:\\ngram_lexer\\sogou_input\\res_sorted_20w.txt', 'r', encoding='utf-8') as r:
    with open('G:\\ngram_lexer\\sogou_input\\res_20w_0807.txt', 'w', encoding='utf-8') as w:
        for item in r:
            items = item.strip().split('\t')
            before = len(base_set)
            base_set.add(items[0])
            after = len(base_set)
            if after > before:
                now = items[0] + '\t' + items[1]
                print(now)
                w.write(now)
                w.write('\n')
                w.flush()
