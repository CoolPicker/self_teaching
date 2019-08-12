#!/usr/bin/env python
# encoding: utf-8
"""
@author: Peter Wick
@license: (C) Copyright 2018-2020, Rosetta Lab Limited.
@contact: niuya312@gmail.com
@file: chose_word_baidu_dict.py
@time: 2019-7-26 20:24
@desc:
"""

import requests
from bs4 import BeautifulSoup
import unicodedata
import sys

proxies = {
    "http": "http://113.120.36.104:808"  # 代理ip
}

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
                  "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Referer": "http://www.xicidaili.com/nn/1"
}


def word_pinyin(wordRes):
    url = 'https://dict.baidu.com/s?wd=' + wordRes + '&from=zici&tn=sug_click'
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
            if each:
                each = unicodedata.normalize('NFKD', each).encode('ascii', 'ignore')
                each = each.decode()
    except:
        each = ''
    return each


if __name__ == "__main__":
    inputPath = sys.argv[1]
    outputPath = sys.argv[2]
    with open(inputPath, 'r', encoding='utf-8') as f:
        with open(outputPath, 'w', encoding='utf-8') as w:
            for item in f:
                item = item.strip()
                res = word_pinyin(item)
                if res:
                    w.write(item)
                    w.write('\n')
                    w.flush()

