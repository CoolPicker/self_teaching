#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

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
            if each:
                each = unicodedata.normalize('NFKD', each).encode('ascii', 'ignore')
                each = each.decode()
    except:
        each = ''
    return each


def res_get():
    with open('G:\\666.txt', 'w', encoding='utf-8') as w:
        with open('G:\\tt.txt', 'r', encoding='utf-8') as f:
            for ii in f:
                word = ii.strip()
                items = word.split('\t')
                first = items[0]
                req = '“'+first+'”'
                res = word_pinyin(req)
                now = first + '\t' + res
                print(now)
                if res and len(first) == len(res.split(' ')):
                    w.write(now)
                    w.write('\n')
                    w.flush()
                else:
                    continue


res_get()
