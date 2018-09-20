# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class ItbenetPipelineJSON(object):
	def __init__(self):
		self.file=open("teachers.json",'wb')
	def process_item(self, item, spider):
		str=json.dumps(dict(item),ensure_ascii=False)+"\n"
		self.file.write(str.encode("utf-8"))
		return item
	def close_spider(self,spider):
		self.file.close()

class ItbenetPipelineTXT(object):
	def __init__(self):
		self.file=open("teachers.txt",'wb')
	def process_item(self, item, spider):
		#str=json.dumps(dict(item),ensure_ascii=False)+"\n"
		
		str=item['name']+"\t"+item['info']+"\n"
		self.file.write(str.encode("utf-8"))
		return item
	def close_spider(self,spider):
		self.file.close()