import scrapy as scr
import scrapy.spiders as spi
import scrapy.linkextractors as lx
import scrapy.shell as scs

class COIndependentSpider(scr.Spider):
    name = 'ColoradoIndependent'
    
    allowed_domains = ['coloradoindependent.com']
    start_urls = ['http://www.coloradoindependent.com/feed']

    def parse(self, response):

        scs.inspect_response(response, self)
        titles = response.xpath('//channel/item/title/text()')
        links = response.xpath('//channel/item/link/text()')

        for link in links:
            yield scr.Request(link.extract(), callback=self.parse_page)

    def parse_page(self, response):
        scs.inspect_response(response, self)

        pars = [p.extract() for p in response.xpath('//p[not(@class) and not(@style)]')]



