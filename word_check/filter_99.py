#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

new_check = set()
with open('G:\\base_dict_21w.txt', 'r', encoding='utf-8') as r:
    for item in r:
        items = item.strip()
        if items in new_check:
            print(items)
        else:
            new_check.add(items)

print(len(new_check))