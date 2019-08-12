#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

from string import digits
remove_digits = str.maketrans('', '', digits)

with open('G:\\ngram_lex_base.txt', 'r', encoding='utf-8') as r:
    with open('G:\\11.txt', 'w', encoding='utf-8') as w:
        for item in r:
            items = item.strip().split('\t')
            first = items[0]
            second = items[1].translate(remove_digits)
            third = items[2]
            each = first+'\t'+second+'\t'+third
            print(each)
            w.write(each)
            w.write('\n')
            w.flush()