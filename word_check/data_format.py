#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: data_format.py
@time: 2019-7-18 13:20
@desc:
"""
import re
import string
from zhon.hanzi import punctuation as punct_chs

with open('G:\\标注数据集\\人民日报\\pd\\pd.train', 'r', encoding='utf-8') as r:
    with open('G:\\rmrb_news.txt', 'w', encoding='utf-8') as w:
        i = 0
        for item in r:
            print(str(i))
            i = i + 1
            item = item.strip()
            item = item.replace(' ', '')
            item = re.sub("\[.*?\]+", '', item, flags=re.U)
            item = re.sub("[%s%s]+" % (punct_chs, string.punctuation), "\n", item.strip(), flags=re.U)  # 替换标点为换行符
            item = re.sub("[^\n\u4E00-\u9FD5]+", "", item, flags=re.U)  # 除中文和 \n ，其余替换为''
            item.replace('\n\n', '\n')
            item = item.strip()
            if item:
                print(item)
                w.write(item)
                w.write('\n')
                w.flush()