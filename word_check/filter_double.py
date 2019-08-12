#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya


now_list = []
with open('G:\\base_dict_20w_filter.txt', 'r', encoding='utf-8') as rf:
    with open('G:\\base_dict_20w_filter_double.txt', 'w', encoding='utf-8') as w:
        for item in rf:
            item = item.strip()
            first = item.split('\t')[0]
            if first in now_list:
                print(item)
            else:
                now_list.append(now_list)
                w.write(item)
                w.write('\n')
                w.flush()