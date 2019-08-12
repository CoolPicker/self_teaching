#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

from pypinyin import lazy_pinyin

import requests
from bs4 import BeautifulSoup
import unicodedata

proxies = {
    "http": "http://113.120.36.104:808"  # 代理ip
}

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Referer": "http://www.xicidaili.com/nn/1"
}


# ü filter
def v_filter(input_word):
    input_word = input_word.replace('ü', 'v')
    input_word = input_word.replace('ǜ', 'v')
    input_word = input_word.replace('ǘ', 'v')
    input_word = input_word.replace('ǚ', 'v')
    input_word = input_word.replace('ǜ', 'v')
    return input_word


def word_pinyin(wordRes):
    url = 'https://dict.baidu.com/s?wd=' + wordRes + '&from=zici'
    each = ''
    try:
        ret = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)
        content = ret.content

        soup = BeautifulSoup(content, 'html.parser')

        form = soup.select('div[id="pinyin"] > h2 > span > b')

        if form:
            each = form[0].get_text().strip()
            each = each.replace('[', '')
            each = each.replace(']', '')
            each = each.strip()
            each = v_filter(each)
            if each:
                each = unicodedata.normalize('NFKD', each).encode('ascii', 'ignore')
                each = each.decode()
    except:
        each = ''
    return each


with open('G:\\sougou_5k.txt', 'r', encoding='utf-8') as f:
    with open('G:\\sougou_5k_py.txt', 'w', encoding='utf-8') as w:
        for item in f:
            item = item.strip()
            length = len(item)
            res = word_pinyin(item)
            if res and length == len(res.split(' ')):
                here = item + '\t' + res + '\t' + str(length) + '\t' + 'baidu-dict'
            else:
                each = ' '.join(lazy_pinyin(item))
                here = item + '\t' + each + '\t' + str(length) + '\t' + 'pypinyin'
            print(here)
            w.write(here)
            w.write('\n')
            w.flush()