#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: key_position_shell.py
@time: 2019-8-1 10:41
@desc:
"""

first_position = '500, 500'

moveTo = 'MoveTo 500, 500'
leftClick = 'LeftClick 1'
keyDown = 'KeyDown '
keyDownSpace = 'KeyDown "Space", 1'
keyDownEnter = 'KeyDown "Enter", 1'


def letters2command(letters):
    res_commands = []
    length = len(letters)
    for i, char in enumerate(letters):
        res_commands.append(keyDown + '"' + char + '", ' + str(1))
        if i == (length - 1):
            res_commands.append(keyDownSpace)
            res_commands.append(keyDownEnter)
            return res_commands


def head2repair(name):
    head_list = ['[General]', 'SyntaxVersion=2', 'BeginHotkey=121', 'BeginHotkeyMod=0', 'PauseHotkey=0',
                 'PauseHotkeyMod=0', 'StopHotkey=123', 'StopHotkeyMod=0', 'EnableWindow=',
                 'MacroID=c63d2afe-83f3-4d04-b846-e0ddd3a20bd6', 'Description=' + name, 'Enable=0', 'AutoRun=0',
                 'Type=0', 'Number=1', '[SetupUI]', 'Type=2', 'QUI=', '[Relative]', 'SetupOCXFile=', '[Comment]', '\n',
                 '[Script] ', moveTo, leftClick]
    return head_list


each = 1000
count = 0
for i in range(3169):
    if i > 0:
        index = 1
        filename = 'res_top_' + str(i) + '_k.Q'
        with open('G:\\ngram_lexer\\sogou_input\\v2_clean_base.txt', 'r', encoding='utf-8') as r:
            with open('G:\\ngram_lexer\\sogou_input\\' + filename, 'w', encoding='utf-8') as w:
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
                        command = '\n'.join(letters2command(pin_yin))
                        w.write(command)
                        w.write('\n')
                        w.flush()

                    index = index + 1


