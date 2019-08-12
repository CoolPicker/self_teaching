#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: lexer_result_operate.py
@time: 2019-7-31 9:34
@desc:
"""

with open('G:\\ngram_lexer\\res_lexer_0731.txt', 'r', encoding='utf-8') as f:
    with open('G:\\ngram_lexer\\result_lexer\\res_loc.txt', 'w', encoding='utf-8') as loc:
        with open('G:\\ngram_lexer\\result_lexer\\res_per.txt', 'w', encoding='utf-8') as per:
            with open('G:\\ngram_lexer\\result_lexer\\res_org.txt', 'w', encoding='utf-8') as org:
                with open('G:\\ngram_lexer\\result_lexer\\res_time.txt', 'w', encoding='utf-8') as tim:
                    with open('G:\\ngram_lexer\\result_lexer\\res_null.txt', 'w', encoding='utf-8') as nul:
                        for item in f:
                            items = item.strip().split('\t')
                            word = items[0].strip()
                            lexer = items[2].strip()
                            if lexer == 'TIME':
                                tim.write(word)
                                tim.write('\n')
                                tim.flush()
                            elif lexer == 'ORG':
                                org.write(word)
                                org.write('\n')
                                org.flush()
                            elif lexer == 'PER':
                                per.write(word)
                                per.write('\n')
                                per.flush()
                            elif lexer == 'LOC':
                                loc.write(word)
                                loc.write('\n')
                                loc.flush()
                            else:
                                nul.write(word)
                                nul.write('\n')
                                nul.flush()


