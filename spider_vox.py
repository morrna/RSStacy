import scrapy

class VoxSpider(scrapy.Spider):
	name = 'Vox'
	start_urls = ['http://www.vox.com/news']

	def parse(self, response):
		trial_class = 'h3'
		for thing in response.css(trial_class):
			yield { trial_class: thing.xpath('//a/@href').extract() }
