import scrapy

class ColoradoanSpider(scrapy.Spider):
	name = 'Coloradoan'
	start_urls = ['http://www.coloradoan.com/news']

	def parse(self, response):
		for href in response.css('.hgpm-link a a::attr(href)'):
			yield href
