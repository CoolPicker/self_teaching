#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

single_set = set()
with open('G:\\0712_name_new.txt', 'r', encoding='utf-8') as r:
    for item in r:
        item = item.strip()
        single_set.add(item)
print(single_set.__len__())
with open('G:\\base_dict_20w_res.txt', 'r', encoding='utf-8') as rf:
    with open('G:\\base_dict_20w_res_1.txt', 'w', encoding='utf-8') as w:
        for item in rf:
            item = item.strip()
            items = item.split('\t')

            sequence = items[0]
            pins = items[1]
            lvs = ['徐', '孙', '马', '朱', '胡',
                   '林', '郭', '何', '高', '罗',
                   '郑', '梁', '谢', '宋', '唐',
                   '许', '邓', '冯', '韩', '曹',
                   '曾', '彭', '萧', '蔡', '潘',
                   '田', '董', '袁', '于', '余',
                   '叶', '蒋', '杜', '苏', '魏',
                   '王', '李', '张', '刘', '陈',
                   '杨', '黄', '赵', '周', '吴',
                   '程', '吕', '丁', '沈', '任']
            pin_arr = pins.split(' ')
            index = 0
            for lv in lvs:
                if sequence[0] == lv:
                    index = 1
                    break
            if index == 1 and (len(pin_arr) == 2 or len(pin_arr) == 3):
                if sequence not in single_set:
                    print(sequence)
                    continue
                else:
                    w.write(item)
                    w.write('\n')
                    w.flush()
            else:
                w.write(item)
                w.write('\n')
                w.flush()
