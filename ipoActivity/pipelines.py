# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class IpoactivityPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="10.100.4.99", port=3306, db="opd_common", user="root", passwd="OPDATA",
                                    charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        company_name = item['company_name']
        if "'" in company_name:
            company_name = '"' + str(company_name) + '"'
        else:
            company_name = "'" + str(company_name) + "'"
        company_info_url = item['company_info_url']
        filed_date = item['filed_date']
        withdrawn_date = item['withdrawn_date']
        company_addr = item['company_addr']
        # 地址存在特殊符号，导致sql错误
        if "'" in company_addr:
            company_addr = '"' + str(company_addr) + '"'
        else:
            company_addr = "'" + str(company_addr) + "'"

        company_pho = item['company_pho']
        company_web = item['company_web']
        # ceo名字包含特殊符号导致的sql错误
        ceo = item['ceo']
        if "'" in ceo:
            ceo = '"' + str(ceo) + '"'
        else:
            ceo = "'" + str(ceo) + "'"
        employees = item['employees']
        state_of_inc = item['state_of_inc']
        fiscal_year_end = item['fiscal_year_end']
        status = item['status']
        proposed_symbol = item['proposed_symbol']
        exchange = item['exchange']
        share_price = item['share_price']
        shares_offered = item['shares_offered']
        offer_amount = item['offer_amount']
        total_expenses = item['total_expenses']
        shares_over_alloted = item['shares_over_alloted']
        shareholder_shares_offered = item['shareholder_shares_offered']
        shares_outstanding = item['shares_outstanding']
        lockup_period = item['lockup_period']
        lockup_expiration = item['lockup_expiration']
        quiet_period_expiration = item['quiet_period_expiration']
        cik = item['cik']
        insert_sql = "insert into USA_IPO_activity (company_name, company_info_url, filed_date, withdrawn_date, " \
                     "company_addr, company_pho, company_web, ceo, employees, state_of_inc, fiscal_year_end, status," \
                     "proposed_symbol, exchange, share_price, shares_offered, offer_amount, total_expenses, " \
                     "shares_over_alloted, shareholder_shares_offered, shares_outstanding, lockup_period, lockup_expiration," \
                     "quiet_period_expiration, cik) values ({company_name}, '{company_info_url}', '{filed_date}', " \
                     "'{withdrawn_date}', {company_addr}, '{company_pho}', '{company_web}', {ceo}, '{employees}'," \
                     "'{state_of_inc}', '{fiscal_year_end}', '{status}', '{proposed_symbol}', '{exchange}', '{share_price}'," \
                     "'{shares_offered}', '{offer_amount}', '{total_expenses}', '{shares_over_alloted}', '{shareholder_shares_offered}'," \
                     "'{shares_outstanding}', '{lockup_period}', '{lockup_expiration}', '{quiet_period_expiration}', '{cik}')"\
            .format(company_name=company_name, company_info_url=company_info_url, filed_date=filed_date, withdrawn_date=withdrawn_date,
                company_addr=company_addr, company_pho=company_pho, company_web=company_web, ceo= ceo, employees=employees,
                state_of_inc=state_of_inc, fiscal_year_end=fiscal_year_end, status=status, proposed_symbol=proposed_symbol,
                exchange=exchange, share_price=share_price, shares_offered=shares_offered, offer_amount=offer_amount,
                total_expenses=total_expenses, shares_over_alloted=shares_over_alloted,
                shareholder_shares_offered=shareholder_shares_offered, shares_outstanding=shares_outstanding,
                lockup_period=lockup_period, lockup_expiration=lockup_expiration, quiet_period_expiration=quiet_period_expiration,
                cik=cik)
        try:
            self.cursor.execute(insert_sql)
            self.conn.commit()
            print('新增' + company_name)
        except:
            print('语法错误:'+ insert_sql)
            with open('sqlErrorCompanyList.csv', 'a+', encoding='utf-8') as f:
                f.write('sql语法错误'+insert_sql + '||' + company_info_url +'\n')
                f.close()

        return item

    def close_spider(self, spider):
        """Discard the database pool on spider close"""
        self.cursor.close()
        self.conn.close()