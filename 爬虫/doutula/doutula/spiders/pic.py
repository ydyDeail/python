# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doutula.items import DoutulaItem

class PicSpider(CrawlSpider):
    name = 'pic'
    allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com/photo/list/?page=1']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        pics=response.xpath('//div[@class="page-content text-center"]/div/a')
        for pic in pics:
            item=DoutulaItem()
            item['img_url']=pic.xpath("./img/@data-original").extract()[0]
            item['name']=pic.xpath("./p/text()").extract()[0]
            #print(item)
            yield item

