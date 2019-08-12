#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: mobile_key_single_pinyin.py
@time: 2019-8-5 10:44
@desc:
"""
keyDown = 'KeyDown '
keyDownSpace = 'KeyDown "Space"'
keyDownEnter = 'KeyDown "Enter"'


def letters2command(letters):
    res_commands = []
    length = len(letters)
    for i, char in enumerate(letters):
        res_commands.append(keyDown + '"' + char + '"')
        if i == (length - 1):
            res_commands.append(keyDownSpace)
            res_commands.append(keyDownEnter)
            return res_commands


each = 1000
count = 0
for i in range(2306):
    if i > 0:
        index = 1
        filename = 'res_top_' + str(i+200) + '_k.Q'
        with open('G:\\ngram_lexer\\sogou_input\\ngram_20w_others_single.txt', 'r', encoding='utf-8') as r:
            with open('G:\\ngram_lexer\\sogou_input\\single\\' + filename, 'w', encoding='utf-8') as w:
                w.write('Delay 1000')
                w.write('\n')
                w.flush()
                for item in r:
                    if (i-1) * each < index <= i * each:
                        count = count + 1
                        print(count)
                        item = item.strip()
                        pin_yin = ''.join(item.split(' '))
                        command = '\n'.join(letters2command(pin_yin))
                        w.write(command)
                        w.write('\n')
                        w.flush()

                    index = index + 1


