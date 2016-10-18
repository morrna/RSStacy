import scrapy as scr
import scrapy.spiders as spi
import scrapy.linkextractors as lx

class ColoradoanSpider(spi.CrawlSpider):
        name = 'Coloradoan'
        allowed_domains = ['coloradoan.com']
        start_urls = ['http://www.coloradoan.com/news']
        
        rules = [ spi.Rule(lx.LinkExtractor(allow='story/news'))
                ]

        def parse_item(self, response):
            scr.inspect_response(response, self)
