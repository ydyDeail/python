# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent2.items import Tencent2Item


class TencentSpider(CrawlSpider):
    name = 'Tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    pageLink=LinkExtractor(allow=r'start=\d+')
    infoLink=LinkExtractor(allow=r'position_detail\.php')
    rules = (
        Rule(pageLink, callback='parse_position', follow=True),
        Rule(infoLink, callback='parse_info', follow=True),
        
    )
    def parse_info(self,response):
        item=Tencent2Item()
        item['name']=response.xpath('//table[@class="tablelist textl"]/tr[1]/td[1]/text()').extract()[0]
        item['duty']=','.join(response.xpath('//ul[@class="squareli"]')[0].xpath("./li/text()").extract())
        item['require']=','.join(response.xpath('//ul[@class="squareli"]')[1].xpath("./li/text()").extract())
        yield item
    def parse_position(self,response):
        pass
