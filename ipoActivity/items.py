# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpoactivityItem(scrapy.Item):
    company_name = scrapy.Field()
    company_info_url = scrapy.Field()
    filed_date = scrapy.Field()
    withdrawn_date = scrapy.Field()
    company_addr = scrapy.Field()
    company_pho = scrapy.Field()
    company_web = scrapy.Field()
    ceo = scrapy.Field()
    employees = scrapy.Field()
    state_of_inc = scrapy.Field()
    fiscal_year_end = scrapy.Field()
    status = scrapy.Field()
    proposed_symbol = scrapy.Field()
    exchange = scrapy.Field()
    share_price = scrapy.Field()
    shares_offered = scrapy.Field()
    offer_amount = scrapy.Field()
    total_expenses = scrapy.Field()
    shares_over_alloted = scrapy.Field()
    shareholder_shares_offered = scrapy.Field()
    shares_outstanding = scrapy.Field()
    lockup_period = scrapy.Field()
    lockup_expiration = scrapy.Field()
    quiet_period_expiration = scrapy.Field()
    cik = scrapy.Field()

