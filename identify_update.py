#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nya

"""
身份证编码Excel解析入库MySQL
"""

import xlrd
import pymysql

db = pymysql.connect(host="10.10.198.186", user="root", passwd="shr0$ett@l@b", db="video_retrieval", charset="utf8")

cursor = db.cursor()

path = 'E:\\identify_pre_code_excel.xlsx'

data = xlrd.open_workbook(path)

table = data.sheets()[0]

table_rows = table.nrows

'''
  `six_code` int(6) NOT NULL,
  `four_code` int(4) NOT NULL,
  `certificate_area` varchar(100) DEFAULT NULL,
  `identify_province` varchar(30) DEFAULT NULL,
  `identify_city` varchar(30) DEFAULT NULL,
  `identify_area` varchar(30) DEFAULT NULL,
'''

for i in range(table_rows):
    if i > 0:
        line = table.row_values(i)
        six_code = line[0]
        four_code = line[1]
        certificate_area = line[2]
        identify_province = line[3]
        identify_city = line[4]
        identify_area = line[5]
        print(six_code, four_code, certificate_area, identify_province, identify_city, identify_area)
        sql = '''INSERT INTO identify_code_pre(
            six_code, four_code, certificate_area, identify_province, identify_city, identify_area) 
            VALUES (%s,%s,"%s","%s","%s","%s")'''\
              % (six_code, four_code, certificate_area, identify_province, identify_city, identify_area)
        print(sql)
        cursor.execute(sql)
        db.commit()

db.close()


