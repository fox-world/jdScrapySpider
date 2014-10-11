#-*-coding:utf-8-*-

from scrapy.spider import Spider
from scrapy.selector import Selector

class JdSpider(Spider):

	name="jdSpider"
	allowed_domains=["jd.com"]
	start_urls=["http://search.jd.com/Search?keyword=Java&enc=utf-8"]

	def parse(self,response):
		sel=Selector(response)
		names=sel.xpath("//div[@class='p-name']/a/text()").extract()
		for name in names:
			print name.strip('\t\n\r')