#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: baidu_word_character.py
@time: 2019-7-29 11:18
@desc:
"""
import requests
import json
import time
import sys

headers = {
    "Content-Type": "application/json; charset=UTF-8"
}
client_id = 'SLAhajs7DbGNe3ZkDryX54S3'
client_secret = 'luABREStKPE5oyng34OY0ZbslBDDwcRp'


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
    host = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token=' + access_token
    req = {'text': word}
    res_lexer = requests.post(host, headers=headers, data=json.dumps(req))
    result = str(res_lexer.content, encoding='utf-8')
    return result


with open('G:\\ngram_lexer\\test\\v2_base_split_05.txt', 'r', encoding='utf-8') as r:
    with open('G:\\ngram_lexer\\test\\res_05.txt', 'w', encoding='utf-8') as w:
        size_limit = 22000
        limit_last = ''
        each_operate = ''
        operate_last = ''
        size = 0
        index = 1
        for item in r:
            item = item.strip()
            index = index + 1
            operate_last = each_operate
            if each_operate:
                each_operate = each_operate + ' ' + item
                size = size + 1
            else:
                each_operate = item
            if sys.getsizeof(each_operate) >= size_limit or index > 449468:
                time.sleep(0.5)
                res = get_key_character(operate_last + " ")
                each_operate = item
                size = 0

                lexer = json.loads(res)
                items = lexer['items']
                length = len(items)

                here = ''
                count = 0
                for item_each in items:
                    now = item_each['item']
                    if now == ' ':
                        if count == 1:
                            ne = here_before['ne']
                            if ne:
                                ne = ne
                            else:
                                ne = 'null'
                            write_line = here_before['item'] + '\t' + str(count) + '\t' + ne
                        else:
                            write_line = here + '\t' + str(count) + '\t' + 'null'
                        print(write_line)
                        w.write(write_line)
                        w.write('\n')
                        w.flush()
                        count = 0
                        here = ''
                    else:
                        count = count + 1
                        if here:
                            here = here + item_each['item']
                        else:
                            here = item_each['item']
                    here_before = item_each


                # res = get_key_character(item)
                # lexer = json.loads(res)
                # items = lexer['items']
                # length = len(items)
                # ne = 'null'
                # if length == 1:
                #     then = items[0]
                #     character = then['ne']
                #     if character:
                #         ne = character
                # last = item + '\t' + str(length) + '\t' + ne
                # w.write(last)
                # w.write('\n')
                # w.flush()



# if __name__ == "__main__":
#     if len(sys.argv) < 5:
#         sys.exit(-1)
#     inputPath = sys.argv[1]
#     outputPath = sys.argv[2]
#     client_id = sys.argv[3]
#     client_secret = sys.argv[4]
#     with open(inputPath, 'r', encoding='utf-8') as r:
#         with open(outputPath, 'w', encoding='utf-8') as w:
#             for item in r:
#                 time.sleep(0.5)
#                 item = item.strip()
#                 res = get_key_character(item)
#                 lexer = json.loads(res)
#                 items = lexer['items']
#                 length = len(items)
#                 ne = 'null'
#                 if length == 1:
#                     then = items[0]
#                     character = then['ne']
#                     if character:
#                         ne = character
#                 last = item + '\t' + str(length) + '\t' + ne
#                 w.write(last)
#                 w.write('\n')
#                 w.flush()


