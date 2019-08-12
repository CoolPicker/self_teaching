#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: pointer_position.py
@time: 2019-7-31 19:13
@desc:
"""

position_dict = {'1': '477, 532',
                 '2': '789, 532',
                 '3': '1109, 532',
                 '4': '477, 646',
                 '5': '789, 646',
                 '6': '1109, 646',
                 '7': '477, 758',
                 '8': '789, 758',
                 '9': '1109, 758',
                 '0': '789, 872'}

moveTo = 'MoveTo '
leftClick = 'LeftClick 1'


def num2command(num):
    res_commands = []
    length = len(num)
    for i, char in enumerate(num):
        now_position = position_dict[char]
        res_commands.append(moveTo + now_position)
        res_commands.append(leftClick)
        if i == (length - 1):
            res_commands.append(moveTo + position_dict['0'])
            res_commands.append(leftClick)
            res_commands.append(moveTo + position_dict['0'])
            res_commands.append(leftClick)
            return res_commands


position_dict_26 = {'q': '88, 536',
                    'w': '248, 536',
                    'e': '406, 536',
                    'r': '565, 536',
                    't': '721, 536',
                    'y': '878, 536',
                    'u': '1039, 536',
                    'i': '1195, 536',
                    'o': '1354, 536',
                    'p': '1512, 536',
                    'a': '169, 650',
                    'l': '1432, 650',
                    's': '326, 650',
                    'd': '487, 650',
                    'f': '645, 650',
                    'g': '802, 650',
                    'h': '960, 650',
                    'j': '1123, 650',
                    'k': '1274, 650',
                    'z': '326, 764',
                    'x': '487, 764',
                    'c': '645, 764',
                    'v': '802, 764',
                    'b': '960, 764',
                    'n': '1123, 764',
                    'm': '1274, 764',
                    '0': '805, 876',
                    '1': '1476, 876'}


def letters2command(letters):
    res_commands = []
    length = len(letters)
    for i, char in enumerate(letters):
        now_position = position_dict_26[char]
        res_commands.append(moveTo + now_position)
        res_commands.append(leftClick)
        if i == (length - 1):
            res_commands.append(moveTo + position_dict_26['0'])
            res_commands.append(leftClick)
            res_commands.append(moveTo + position_dict_26['1'])
            res_commands.append(leftClick)
            return res_commands


def head2repair(name):
    head_list = ['[General]', 'SyntaxVersion=2', 'BeginHotkey=121', 'BeginHotkeyMod=0', 'PauseHotkey=0',
                 'PauseHotkeyMod=0', 'StopHotkey=123', 'StopHotkeyMod=0', 'EnableWindow=',
                 'MacroID=c63d2afe-83f3-4d04-b846-e0ddd3a20bd6', 'Description=' + name, 'Enable=0', 'AutoRun=0',
                 'Type=0', 'Number=1', '[SetupUI]', 'Type=2', 'QUI=', '[Relative]', 'SetupOCXFile=', '[Comment]', '\n',
                 '[Script] ']
    return head_list


# command_here = '\n'.join(letters2command('woshizhongguoren'))
# print(command_here)
each = 1000
# i = 1


count = 0
for i in range(3169):
    if i > 0:
        index = 1
        filename = 'pointer_res_top_' + str(i) + '_k.Q'
        with open('G:\\ngram_lexer\\sogou_input\\v2_clean_base.txt', 'r', encoding='utf-8') as r:
            with open('G:\\ngram_lexer\\sogou_input\\pointer\\' + filename, 'w', encoding='utf-8') as w:
                w.write('\n'.join(head2repair(filename)))
                w.write('\n')
                w.flush()
                for item in r:
                    if (i-1) * each < index <= i * each:
                        count = count + 1
                        print(count)
                        item = item.strip()
                        items = item.split('\t')
                        pins = items[1].strip()
                        pin_yin = ''.join(pins.split(' '))
                        # print(pin_yin)
                        command = '\n'.join(letters2command(pin_yin))
                        w.write(command)
                        w.write('\n')
                        w.flush()
                    index = index + 1
