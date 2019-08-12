def gen_list(min: int,
             max: int,
             average_min: int,
             average_max: int,
             size: int) -> list:
    """
    生成符合条件的数列
    :param min: 最小值
    :param max: 最大值
    :param size: 数列长度
    :param average_min: 平均值下限
    :param average_max: 平均值上限
    :return: list
    """
    import random
    average = (average_min + average_max) / 2
    num_list = [random.randint(min, max) for i in range(size)]
    sum_min = average_min * size
    sum_max = average_max * size
    num_sum = sum(num_list)
    i = 0
    while num_sum > sum_max or num_sum < sum_min:
        i += 1
        print('iteration[{}]'.format(i))
        # iterate num list
        random.shuffle(num_list)
        if num_sum > sum_max:
            num_list[0] = random.randint(min, average)
        elif num_sum < sum_min:
            num_list[0] = random.randint(average, max)
        num_sum = sum(num_list)

    return num_list


if __name__ == '__main__':

    some_list = gen_list(min=1,
                         max=100,
                         average_min=9,
                         average_max=11,
                         size=20)
    print(some_list)
    print(sum(some_list))
    print(sum(some_list) / len(some_list))


