from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"

from pypinyin import pinyin, lazy_pinyin, Style
from random import randrange

idiom_dic = {}
idiom_list = []
idiom_char_dic = {}

with open('E:\python_workspace\coal_dict.txt', 'r', encoding='utf8') as r:
    for line in r:
        line = line.strip()
        if None == line or line == '':
            continue
        idiom_list.append(line)
        key = lazy_pinyin(line)[0]
        value = ''
        if key in idiom_dic.keys():
            value = idiom_dic[key] + ',' + line
        else:
            value = line
        idiom_dic[key] = value
        # 汉字接龙
        key_char = line[0]
        value_char = ''
        if key_char in idiom_char_dic.keys():
            value_char = idiom_char_dic[key_char] + ',' + line
        else:
            value_char = line
        idiom_char_dic[key_char] = value_char


# 汉字接龙
def idiom_next_char(idiom, polyphone=False):
    if idiom not in idiom_list:
        res = idiom + ' is not one idiom'
    else:
        last = idiom[len(idiom) - 1]
        if polyphone:
            pass
            if last not in idiom_char_dic:
                res = 'library without the supply idioms'
            else:
                aa = idiom_char_dic[last]
                last = lazy_pinyin(idiom)[len(idiom) - 1]
                bb = idiom_dic[last]
                aa_list = aa.split(',')
                bb_list = bb.split(',')
                cd_list = set(aa_list).intersection(set(bb_list))  # 求并集
                res = ','.join(cd_list)
        else:
            if last not in idiom_char_dic:
                res = 'library without the supply idioms'
            else:
                res = idiom_char_dic[last]
    return res


# 拼音接龙
def idiom_next(idiom):
    if idiom not in idiom_list:
        res = idiom + ' is not one idiom'
    else:
        last = lazy_pinyin(idiom)[len(idiom) - 1]
        if last not in idiom_dic:
            res = 'library without the supply idioms'
        else:
            res = idiom_dic[last]
    return res


# print(idiom_next('怒发冲冠'))

# 汉字定长接龙
def idiom_multi_char_length(idiom, length=10, polyphone=False):
    index = 0
    res_list = [idiom]
    while index < length:
        res = idiom_next_char(idiom, polyphone)
        if 'idiom' in res:
            break
        else:
            res_next = res.split(',')
            idiom = res_next[0]
        res_list.append(idiom)
        index = index + 1
    return res_list


# 拼音定长接龙
def idiom_multi_length(idiom, length=10):
    index = 0
    res_list = [idiom]
    while index < length:
        res = idiom_next(idiom)
        if 'idiom' in res:
            break
        else:
            res_next = res.split(',')
            idiom = res_next[0]
        res_list.append(idiom)
        index = index + 1
    return res_list


def check_none_follow_list():
    none_follow = []
    for idiom in idiom_list:
        res = idiom_next(idiom)
        if 'idiom' in res:
            none_follow.append(idiom)
    return none_follow


# none_supply = check_none_follow_list()
# print(none_supply)
# 随机出成语
def random_idiom(idiom=None, game=3, init=False):
    if init:
        return idiom_list[randrange(0, len(idiom_list))]
    else:
        if idiom not in idiom_list:
            return 'no'
        else:
            if game == 1:
                idiom_str = idiom_next(idiom)
            elif game == 2:
                idiom_str = idiom_next_char(idiom)
            else:
                idiom_str = idiom_next_char(idiom, polyphone=True)
            res_list = idiom_str.split(',')
            return res_list[randrange(0, len(res_list))]


def random_idioms_str(idiom=None, game=3):
    if game == 1:
        idiom_str = idiom_next(idiom)
    elif game == 2:
        idiom_str = idiom_next_char(idiom)
    else:
        idiom_str = idiom_next_char(idiom, polyphone=True)
    return idiom_str


def puzzle_game():
    print('---- Chinese string up puzzle ----')
    first = input('谁先手？（0 - 玩家  1 - 电脑）：')
    size = 3
    while size > 0:
        first = int(first)
        if type(first) == int:
            if first == 1 or first == 0:
                break
            else:
                first = input('格式错误，请重新输入：')
        size = size - 1
    if size == 0:
        print('bye bye')
        return
    second = input('总轮数：')
    size = 3
    while size > 0:
        second = int(second)
        if type(second) == int:
            break
        else:
            second = input('格式错误，请重新输入：')
        size = size - 1
    if size == 0:
        print('bye bye')
        return
    third = input('游戏类型（拼音匹配 - 1 ， 汉字匹配 - 2 ， 拼音汉字双匹配 - 3）：')
    size = 3
    while size > 0:
        third = int(third)
        if type(third) == int:
            break
        else:
            third = input('格式错误，请重新输入：')
        size = size - 1
    if size == 0:
        print('bye bye')
        return
    print('先手：{}，轮数：{}，游戏类型：{}'.format(first, second, third))
    res_list = []
    init = 0
    while second > 0:
        idiom = ''
        if first == 1:
            res_str = random_idiom(init=True)
            print('you：' + res_str)
            res_list = random_idioms_str(res_str, third).split(',')
            first = 2
            init = 1
        elif first == 0:
            idiom = input('me ：')
        if init != 1:
            # 初次输入，校验是否为成语
            if len(res_list) == 0:
                total = 3
                while total > 0:
                    res_random = random_idiom(idiom, third)
                    if res_random != 'no':
                        print('you：' + res_random)
                        break
                    else:
                        idiom = input('非成语，请重新输入：')
                    total = total - 1
                res_list = random_idioms_str(idiom, third).split(',')
                if total < 0:
                    print('bye bye')
                    return
            else:
                now_total = 3
                while now_total > 0:
                    if now_total == 3:
                        idiom = input('me ：')
                    else:
                        if idiom not in res_list:
                            idiom = input('未接上，请重新输入：')
                        else:
                            print(idiom)
                            break
                    now_total = now_total - 1
                if now_total < 0:
                    print('bye bye')
                    return
                total = 3
                while total > 0:
                    res_random = random_idiom(idiom, third)
                    if res_random != 'no':
                        print('you：' + res_random)
                        break
                    else:
                        idiom = input('非成语，请重新输入：')
                    total = total - 1
                res_list = random_idioms_str(res_random, third).split(',')
                if total < 0:
                    print('bye bye')
                    return
        print('轮数：' + str(second))
        init = 2
        second = second - 1
    print('you win')


# puzzle_game()

