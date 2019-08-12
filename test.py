def puzzle_game():
    print('---- Chinese string up puzzle ----')
    first = input('谁先手？（0 - 玩家  1 - 电脑）：')
    size = 3
    while size > 0:
        if type(first) == int:
            if first == 1 or first == 0:
                break
        else:
            first = input('格式错误，请重新输入：')
        size = size - 1
    if size < 0:
        print('bye bye')
        return
    second = input('总轮数：')
    size = 3
    while size > 0:
        if type(second) == int:
            break
        else:
            second = input('格式错误，请重新输入：')
        size = size - 1
    if size < 0:
        print('bye bye')
        return
    third = input('游戏类型（拼音匹配 - 1 ， 汉字匹配 - 2 ， 拼音汉字双匹配 - 3）：')
    size = 3
    while size > 0:
        if type(third) == int:
            break
        else:
            third = input('格式错误，请重新输入：')
        size = size - 1
    if size < 0:
        print('bye bye')
        return


puzzle_game()