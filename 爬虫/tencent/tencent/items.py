# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	name = scrapy.Field()
	#链接
	link = scrapy.Field()
	#类别
	type = scrapy.Field()
	#人数
	num = scrapy.Field()
	#地点
	location = scrapy.Field()
	#时间
	time = scrapy.Field()
	duty=scrapy.Field()
	require=scrapy.Field()
