#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: baidu_ocr.py
@time: 2019-8-19 18:05
@desc:
"""

import requests
import json
import time
import sys
import os
import base64
import urllib
import os
from urllib3 import encode_multipart_formdata
import requests
import json

headers = {
    "Content-Type": "application/json; charset=UTF-8"
}
client_id = '5zGGo9HrVsYRpOwLIYvF4Gbs'
client_secret = 'FQoDxVF16ZmeT34X7CDNNsmyuX1prKcp'


def access_token_get():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
           client_id + \
           '&client_secret=' + client_secret
    res_token = requests.post(host, headers=headers)
    result = str(res_token.content, encoding='utf-8')
    return result


token_dict_str = access_token_get()
token_dict = json.loads(token_dict_str)
access_token = token_dict['access_token']


def get_key_character(word):
    host = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?charset=UTF-8&access_token=' + access_token
    req = {'image': word}
    res_lexer = requests.post(host, headers=headers, data=req)
    result = str(res_lexer.content, encoding='utf-8')
    return result


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


path = 'G:\\qujianpan\\9-3\\'
with open('G:\\qujianpan\\9-3.txt', 'w', encoding='utf-8') as w:
    for item in os.listdir(path):
        file_name = item.strip()
        names = file_name.split('.')
        pins = names[0]
        with open(path + file_name, 'rb') as f:
            base64_data = base64.b64encode(f.read())
            res = get_key_character(base64_data)
            resp = json.loads(res)
            dataBaidu = resp['words_result'][0]['words']
            resLocal = word_check_file(file_name, path + file_name)
            respLocal = json.loads(resLocal)
            dataLocal = respLocal['data']
            firstThreeLocal = dataLocal.split(' ')[:3]
            if dataBaidu[:3] != dataLocal[:3]:
                conditionRes = dataBaidu.split(dataLocal[:2])
                if conditionRes[0]:
                    if dataBaidu[:2] == dataLocal[:2]:
                        headOne = dataLocal[:2] + conditionRes[0]
                    else:
                        headOne = conditionRes[0]
                else:
                    if dataBaidu[:2] == dataLocal[:2]:
                        headOne = dataLocal[:2] + conditionRes[1]
                    else:
                        headOne = conditionRes[1]
                secondOne = firstThreeLocal[0]
                thirdOne = firstThreeLocal[1]
            else:
                headOne = firstThreeLocal[0]
                secondOne = firstThreeLocal[1]
                thirdOne = firstThreeLocal[2]
            print(headOne)
            each = pins + '\t' + headOne + ' ' + secondOne + ' ' + thirdOne
            w.write(each)
            w.write('\n')
            w.flush()