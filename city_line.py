#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

path = 'G:\\city_line.txt'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


with open(path, 'r', encoding='utf8') as f:
    each = 'null'
    count = 0
    for line in f:
        line = line.strip()
        if line != '':
            arr = line.split('\t')
            if len(arr) > 1:
                if is_number(arr[0]):
                    arr.pop(0)
                print(str(arr))
                count = count + 1

    print(count)


