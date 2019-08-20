#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: word_image_calculate.py
@time: 2019-7-22 14:41
@desc:
"""

import os
from urllib3 import encode_multipart_formdata
import requests
import json


def word_check_file(filename, filepath):
    data_ocr = {}
    header = {}
    data_ocr['file'] = (filename, open(filepath, 'rb').read())
    encode_data = encode_multipart_formdata(data_ocr)
    data_ocr = encode_data[0]
    header['Content-Type'] = encode_data[1]
    url = 'http://10.19.9.115:58088/image/file'
    r = requests.post(url, headers=header, data=data_ocr)
    return str(r.content, encoding='utf-8')


path = 'G:\\qujianpan\\9-1\\'
with open('G:\\qujianpan\\9-1.txt', 'w', encoding='utf-8') as w:
    for item in os.listdir(path):
        file_name = item.strip()
        names = file_name.split('.')
        pins = names[0]
        res = word_check_file(file_name, path + file_name)
        resp = json.loads(res)
        data = resp['data']
        data = ' '.join(data.split(' ')[:3])
        each = pins + '\t' + data
        print(each)
        w.write(each)
        w.write('\n')
        w.flush()


