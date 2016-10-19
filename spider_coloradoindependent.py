import scrapy as scr
import scrapy.spiders as spi
import scrapy.linkextractors as lx

class COIndependentSpider(scr.Spider):
    name = 'ColoradoIndependent'
    
    allowed_domains = ['coloradoindependent.com']
    start_urls = ['http://www.coloradoindependent.com/feed']

    def parse(self, response):
        scr.inspect_response(response, self)

