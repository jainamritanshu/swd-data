# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SwdItem(scrapy.Item):
	st_name = scrapy.Field()
	st_id = scrapy.Field()
 