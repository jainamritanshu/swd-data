import scrapy
from swd.items import SwdItem

class swdspider(scrapy.Spider):
	name = 'swd'
	allowed_domains = ["http://swd/"]
	start_urls = ["http://swd/StudentSearch.aspx"]

	def parse(self, response):
		for sel in response.xpath('//td'):
			st_id = sel.xpath('td/text()').extract()
			st_name = sel.xpath('td[2]/text()').extract()
			print st_id, st_name