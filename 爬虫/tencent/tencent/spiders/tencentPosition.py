# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
	name = 'tencentPosition'
	allowed_domains = ['tencent.com']
	url="https://hr.tencent.com/position.php?&start="
	offset=0
	start_urls = [url+str(offset)]

	def parse(self, response):
		positions=response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
		
		for position in positions:
			item=TencentItem()

			item['name']=position.xpath('./td[1]/a/text()').extract()[0]
			print(item['name'])
			item['link']=position.xpath('./td[1]/a/@href').extract()[0]
			#print(item['link'])
			type=position.xpath('./td[2]/text()')
			print(type)
			#tencent中有些类别为空，防止错误
			if len(type)>0:
			    type=type.extract()[0]

			item['type']=type
			item['num']=position.xpath('./td[3]/text()').extract()[0]
			item['location']=position.xpath('./td[4]/text()').extract()[0]
			item['time']=position.xpath('./td[5]/text()').extract()[0] 
			#创建请求对象
			request=scrapy.Request("https://hr.tencent.com/"+item['link'],callback=self.getInfo)
			request.meta['item']=item#传递item对象
			yield request


		if self.offset<1000:

			self.offset+=10
			yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
	#解析详情
	def getInfo(self,response):
		item=response.meta['item']
		item['duty']=','.join(response.xpath('//ul[@class="squareli"]')[0].xpath("./li/text()").extract())
		item['require']=','.join(response.xpath('//ul[@class="squareli"]')[1].xpath("./li/text()").extract())
		yield item;
