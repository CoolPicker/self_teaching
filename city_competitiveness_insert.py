#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

"""
城市竞争力数据入库
"""

import pymysql

db = pymysql.connect(host="10.10.198.186", user="root", passwd="shr0$ett@l@b", db="personal_tailor", charset="utf8")

cursor = db.cursor()
path = 'G:\\city_competitiveness.txt'


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


'''
  `city` varchar(20) DEFAULT NULL COMMENT '城市',
  `economic_competitiveness` double(6,0) DEFAULT NULL COMMENT '经济竞争力',
  `economic_ranking` int(4) DEFAULT NULL COMMENT '经济竞争力排名',
  `sustainable_competitiveness` double(6,0) DEFAULT NULL COMMENT '可持续竞争力',
  `sustainable_ranking` int(4) DEFAULT NULL COMMENT '可持续竞争力排名',
  `livable_competitiveness` double(6,0) DEFAULT NULL COMMENT '宜居城市竞争力',
  `livable_ranking` int(4) DEFAULT NULL COMMENT '宜居竞争力排名',
  `business_environment_competitiveness` double(6,0) DEFAULT NULL COMMENT '营商环境竞争力',
  `business_environment_ranking` int(4) DEFAULT NULL COMMENT '营商环境竞争力排名'
'''


with open(path, 'r', encoding='utf8') as f:
    each = 'null'
    for line in f:
        line = line.strip()
        if line != '':
            if is_number(line):
                each = each + ',' + line
            else:
                if line == '——':
                    each = each + ',' + str(0)
                    continue
                if each != 'null':
                    arr = each.split(',')
                    sql = '''INSERT INTO city_competitiveness(
                                city, 
                                economic_competitiveness, 
                                economic_ranking, 
                                sustainable_competitiveness, 
                                sustainable_ranking, 
                                livable_competitiveness, 
                                livable_ranking, 
                                business_environment_competitiveness, 
                                business_environment_ranking) 
                                VALUES ("%s",%f,%s,%f,%s,%f,%s,%f,%s)''' \
                          % (arr[0], float(arr[1]), arr[2], float(arr[3]), arr[4], float(arr[5]), arr[6], float(arr[7]), arr[8])
                    print(sql)
                    cursor.execute(sql)
                    db.commit()
                each = line

cursor.close()
