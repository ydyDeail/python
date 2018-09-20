# -*- coding: utf-8 -*-
import scrapy
from dundeng.items import DundengItem

class TeacherSpider(scrapy.Spider):
    name = 'Teacher'
    allowed_domains = ['http://www.itbenet.net/szll/index.html']
    start_urls = ['http://www.itbenet.net/szll/index.html']

    def parse(self, response):
        teachers=response.xpath('//div[@class="tea-right"]')
        for t in teachers:
            name=t.xpath('./h5/span/text()').extract()[0]
            info=t.xpath('./p/text()').extract()[0]
            #封装成对象
            item=DundengItem()
            item['name']=name
            item['info']=info
            yield item
        
