# -*- coding: utf-8 -*-
import scrapy

from ipoActivity.utils.date_man import generatePeriods,formatDate

from ipoActivity.items import IpoactivityItem

from ipoActivity.utils.value_man import manage_val


class IpoallSpider(scrapy.Spider):
    name = 'ipoAll'
    allowed_domains = ['www.nasdaq.com']
    start_urls = ['http://www.nasdaq.com/']
    def start_requests(self):
        periods_list = generatePeriods()
        # 正式
        for periods in periods_list:
            url = "https://www.nasdaq.com/markets/ipos/activity.aspx?tab=withdrawn&month=" + periods
            yield scrapy.Request(url=url, callback=self.parse)

        # # 测试
        # url = "https://www.nasdaq.com/markets/ipos/activity.aspx?tab=withdrawn&month=1997-1"
        # yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        company_list = response.xpath('//div[@id="content"]/div[@id="left-column-div"]/'
                                      'div[@class="ipo-wrap"]/div[@class="ipo-tab-content-wrap"]/'
                                      'div[@class="ipo-activity-area panes"]/div[@class="tab4"]/'
                                      'div[@class="genTable"]/table/tbody/tr')
        for company in company_list:
            company_name = company.xpath('./td[1]/a/text()').extract_first()
            company_info_url = company.xpath('./td[1]/a/@href').extract_first()
            # 测试
            # company_info_url = 'https://www.nasdaq.com/markets/ipos/company/peach-auto-painting-collision-inc-34069-7975'
            filed_date = company.xpath('./td[7]/text()').extract_first()
            withdrawn_date = company.xpath('./td[8]/text()').extract_first()
            filed_date = formatDate(filed_date)# 重新格式化日期
            withdrawn_date = formatDate(withdrawn_date)
            yield scrapy.Request(url=company_info_url,
                                 callback=self.parse_companies_info,
                                 meta={'company_name': company_name,
                                       'filed_date': filed_date,
                                       'withdrawn_date': withdrawn_date,
                                       'company_info_url': company_info_url}
                                 )

    def parse_companies_info(self, response):
        company_detail_tr = response.xpath('//div[@id="container"]/div[@id="content"]/div[@id="left-column-div"]/'
                                            'form/div[@id="tabpane1"]/div[@id="infoTable"]/table')

        company_name = response.meta['company_name']
        filed_date = response.meta['filed_date']
        withdrawn_date = response.meta['withdrawn_date']
        company_info_url = response.meta['company_info_url']
        company_addr_list = company_detail_tr.xpath('./tr[2]/td[2]/text()').extract()
        company_addr = '/'.join(company_addr_list)
        company_pho = company_detail_tr.xpath('./tr[3]/td[2]/text()').extract_first()
        # 对空值进行处理
        company_pho = manage_val(company_pho)
        company_web = company_detail_tr.xpath('./tr[4]/td[2]/text()').extract_first()
        company_web = manage_val(company_web)

        ceo = company_detail_tr.xpath('./tr[5]/td[2]/text()').extract_first()
        ceo = manage_val(ceo)
        employees = company_detail_tr.xpath('./tr[6]/td[2]/text()').extract_first()
        employees = manage_val(employees)
        state_of_inc = company_detail_tr.xpath('./tr[7]/td[2]/a/text()').extract_first()
        state_of_inc = manage_val(state_of_inc)
        fiscal_year_end = company_detail_tr.xpath('./tr[8]/td[2]/text()').extract_first()
        fiscal_year_end = manage_val(fiscal_year_end)
        status = company_detail_tr.xpath('./tr[9]/td[2]/text()').extract_first()
        status = manage_val(status)
        proposed_symbol = company_detail_tr.xpath('./tr[10]/td[2]/text()').extract_first()
        proposed_symbol = manage_val(proposed_symbol)
        # 有的交易所没有链接
        exchange = company_detail_tr.xpath('./tr[11]/td[2]/a/text()').extract_first()
        if exchange is None:
            exchange = company_detail_tr.xpath('./tr[11]/td[2]/text()').extract_first()
            exchange = manage_val(exchange)

        share_price = company_detail_tr.xpath('./tr[12]/td[2]/text()').extract_first()
        share_price = manage_val(share_price)
        shares_offered = company_detail_tr.xpath('./tr[13]/td[2]/text()').extract_first()
        shares_offered = manage_val(shares_offered)

        offer_amount = company_detail_tr.xpath('./tr[14]/td[2]/text()').extract_first()
        offer_amount = manage_val(offer_amount)
        total_expenses = company_detail_tr.xpath('./tr[15]/td[2]/text()').extract_first()
        total_expenses = manage_val(total_expenses)

        shares_over_alloted = company_detail_tr.xpath('./tr[16]/td[2]/text()').extract_first()
        shares_over_alloted = manage_val(shares_over_alloted)

        shareholder_shares_offered = company_detail_tr.xpath('./tr[17]/td[2]/text()').extract_first()
        shareholder_shares_offered = manage_val(shareholder_shares_offered)

        shares_outstanding = company_detail_tr.xpath('./tr[18]/td[2]/text()').extract_first()
        shares_outstanding = manage_val(shares_outstanding)

        lockup_period = company_detail_tr.xpath('./tr[19]/td[2]/text()').extract_first()
        lockup_period = manage_val(lockup_period)
        lockup_expiration = company_detail_tr.xpath('./tr[20]/td[2]/text()').extract_first()
        lockup_expiration = manage_val(lockup_expiration)

        quiet_period_expiration = company_detail_tr.xpath('./tr[21]/td[2]/text()').extract_first()
        quiet_period_expiration = manage_val(quiet_period_expiration)
        cik = company_detail_tr.xpath('./tr[22]/td[2]/text()').extract_first()
        cik = manage_val(cik)
        item = IpoactivityItem()
        item['company_name'] = company_name
        item['filed_date'] = filed_date
        item['withdrawn_date'] = withdrawn_date
        item['company_info_url'] = company_info_url
        item['company_addr'] = company_addr
        item['company_pho'] = company_pho
        item['company_web'] = company_web
        item['ceo'] = ceo
        item['employees'] = employees
        item['state_of_inc'] = state_of_inc
        item['fiscal_year_end'] = fiscal_year_end
        item['status'] = status
        item['proposed_symbol'] = proposed_symbol
        item['exchange'] = exchange
        item['share_price'] = share_price
        item['shares_offered'] = shares_offered
        item['offer_amount'] = offer_amount
        item['total_expenses'] = total_expenses
        item['shares_over_alloted'] = shares_over_alloted
        item['shareholder_shares_offered'] = shareholder_shares_offered
        item['shares_outstanding'] = shares_outstanding
        item['lockup_period'] = lockup_period
        item['lockup_expiration'] = lockup_expiration
        item['quiet_period_expiration'] = quiet_period_expiration
        item['cik'] = cik

        yield item







