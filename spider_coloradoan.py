import scrapy

class ColoradoanSpider(scrapy.Spider):
	name = 'Coloradoan'
	start_urls = ['http://www.coloradoan.com/news']

	def parse(self, response):
		trial_class = 'hgpm-link'
		for thing in response.css(trial_class):
			yield { trial_class: thing.extract() }
