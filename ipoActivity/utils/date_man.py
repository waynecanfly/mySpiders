#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import pymysql

conn = pymysql.connect(host="10.100.4.99", port=3306, db="opd_common", user="root", passwd="OPDATA", charset="utf8")
cursor = conn.cursor()

def formatDate(any_date):
    any_date_list = any_date.split('/')
    year, month, day = any_date_list[2], any_date_list[0], any_date_list[1]
    cor_date = year+'-'+month+'-'+day
    return cor_date



def generatePeriods():
    query_usa_ipo = "select max(withdrawn_date) from USA_IPO_activity"
    cursor.execute(query_usa_ipo)
    start_date = cursor.fetchone()
    start_year = start_date[0].year
    start_month = start_date[0].month
    # start_year = 2019
    # start_month = 6
    cur_year = datetime.datetime.now().year
    cur_month = datetime.datetime.now().month
    periods_list = []
    for year in range(int(start_year), int(cur_year) + 1):
        if year == int(start_year):
            for month in range(int(start_month) + 1, int(cur_month) + 1):
                periods = str(year) + '-' + str(month)
                periods_list.append(periods)
        else:
            for month in range(1, 13):
                periods = str(year) + '-' + str(month)
                periods_list.append(periods)

    return periods_list





#
# if __name__ == '__main__':
#     list = generatePeriods02()
#     print(list)
#
#     # generatePeriods02()
