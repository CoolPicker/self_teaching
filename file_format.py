#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

from pypinyin import lazy_pinyin

basePath = 'G:\\222.txt'
dicPath = 'G:\\res.txt'
oneWordPath = 'G:\\single.txt'
twiceAfterPath = 'G:\\triple.txt'
singleBeforePath = 'G:\\beforeSingle.txt'

tripleBeforePath = 'G:\\tripleBefore.txt'
tripleOperatePath = 'G:\\tripleOperate.txt'

realOperatePath = 'G:\\realOperate.txt'
tripleSecondPath = 'G:\\tripleSecond.txt'


# with open(tripleOperatePath, 'r', encoding='utf-8') as f:
#     with open(realOperatePath, 'w', encoding='utf-8') as w:
#         with open(tripleSecondPath, 'w', encoding='utf-8') as ws:
#             for each in f:
#                 each = each.strip()
#                 eachArr = each.split('\t')
#                 word = eachArr[0]
#                 pyArr = eachArr[1].split(' ')
#                 lpArr = lazy_pinyin(word)
#                 for q, a in zip(pyArr, lpArr):
#                     if q != a:
#                         print(each)
#                         w.write(each)
#                         w.write('\n')
#                         w.flush()
#                         break
#                 else:
#                     ws.write(each)
#                     ws.write('\n')
#                     ws.flush()



# word_set = set()
# with open(dicPath, 'r', encoding='utf-8') as f:
#     for each in f:
#         each = each.strip()
#         eachArray = each.split('\t')
#         word = eachArray[0]
#         if len(eachArray[1].split(',')) > 1:
#             word_set.add(word)
#
#
# with open(basePath, 'r', encoding='utf-8') as f:
#     with open(tripleBeforePath, 'w', encoding='utf-8') as wb:
#         with open(tripleOperatePath, 'w', encoding='utf-8') as wo:
#             for now in f:
#                 now = now.strip()
#                 nowArray = now.split('\t')
#                 word = nowArray[1]
#                 pys = nowArray[2]
#                 eachRow = word + '\t' + pys
#                 for letter in word:
#                     if letter in word_set:
#                         wo.write(eachRow)
#                         wo.write('\n')
#                         wo.flush()
#                         break
#                 else:
#                     wb.write(eachRow)
#                     wb.write('\n')
#                     wb.flush()


index = 1
with open(oneWordPath, 'w', encoding='utf-8') as w:
    with open(dicPath, 'r', encoding='utf-8') as f:
        for word in f:
            word = word.strip()
            wordArray = word.split('\t')
            word = wordArray[0]
            pyArray = wordArray[1].split(',')
            for py in pyArray:
                section = str(index) + '\t' + word + '\t' + py
                print(section)
                w.write(section)
                w.write('\n')
                w.flush()
                index = index + 1


wordList = []
with open(oneWordPath, 'r', encoding='utf-8') as fn:
    with open(singleBeforePath, 'r', encoding='utf-8') as fb:
        for each in fn:
            each = each.strip()
            eachArray = each.split('\t')
            word = eachArray[1]
            py = eachArray[2]
            wordEach = word + '\t' + py
            wordList.append(wordEach)
        for before in fb:
            before = before.strip()
            beforeArray = before.split('\t')
            eachTest = beforeArray[1] + '\t' + beforeArray[2]
            if eachTest not in wordList:
                print(eachTest)


