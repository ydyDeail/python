# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
#可转成json文件
class DundengPipelineJSON(object):
	def __init__(self):
		self.file=open("teacher.json",'wb')
	def process_item(self, item, spider):
		str=json.dumps(dict(item),ensure_ascii=False)+"\n"
		self.file.write(str.encode("utf-8"))
		return item
	def close_spider(self,spider):
		self.file.close()
#转成txt文件
class DundengPipelineTXT(object):
	def __init__(self):
		self.file=open("teacher.txt",'wb')
	def process_item(self, item, spider):
		str=item['name']+"\t"+item['info']+"\n"
		self.file.write(str.encode("utf-8"))
		return item
	def close_spider(self,spider):
		self.file.close()