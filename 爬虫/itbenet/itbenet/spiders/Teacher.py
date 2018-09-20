# -*- coding: utf-8 -*-
import scrapy
from itbenet.items import ItbenetItem

class TeacherSpider(scrapy.Spider):
    name = 'Teacher'
    allowed_domains = ['http://www.itbenet.net/szll/index.html']
    start_urls = ['http://www.itbenet.net/szll/index.html']

    def parse(self, response):
        teachers=response.xpath('//div[@class="tea-right"]')
       
        for t in teachers:
        	#获取文本内容
        	name=t.xpath('./h5/span/text()').extract()[0]
        	info=t.xpath('./p/text()').extract()[0]
        	#封装成items对象
        	item=ItbenetItem()
        	item['name']=name
        	item['info']=info
        	yield item
        	
        
        
