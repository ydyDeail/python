# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'Tencent'
    allowed_domains = ['tencent.com']
    offset=0
    url="http://hr.tencent.com/position.php?&start="
    start_urls = [url+str(offset)]
    def parse(self, response):
        positions=response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for position in positions:
        	item=TencentItem()
        	item['name']=position.xpath('./td[1]/a/text()').extract()[0]
        	item['link']=position.xpath('./td[1]/a/@href').extract()[0]
        	type=position.xpath('./td[2]/text()')
        	if len(type)>0:
        		type=type.extract()[0]
        	item['type']=type
        	item['num']=position.xpath('./td[3]/text()').extract()[0]
        	item['location']=position.xpath('./td[4]/text()').extract()[0]
        	item['time']=position.xpath('./td[5]/text()').extract()[0]
        	request=scrapy.Request("https://hr.tencent.com/"+item['link'],callback=self.getinfo)
        	request.meta['item']=item
        	yield request
        if self.offset<1000:
        	self.offset+=10
        	print("*"*50)
        	yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
    def getinfo(self,response):
    	item=response.meta['item']
    	item['duty']=','.join(response.xpath('//ul[@class="squareli"]')[0].xpath("./li/text()").extract())
    	item['require']=','.join(response.xpath('//ul[@class="squareli"]')[1].xpath("./li/text()").extract())
    	yield item;