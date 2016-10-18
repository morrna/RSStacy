import scrapy as scr
import scrapy.spiders as spi
import scrapy.linkextractors as lx

class ColoradoanSpider(scr.Spider):
        name = 'Coloradoan'
        allowed_domains = ['coloradoan.com']
        start_urls = ['http://www.coloradoan.com/news']
        
        good_links = lx.LinkExtractor(allow='story/news')

        def parse(self, response):
            return dict(enumerate([ [link.url, link.text] \
                    for link in self.good_links.extract_links(response) ] ))
