import scrapy
import sys


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow' 
    def __init__(self, tag=None, *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://stackoverflow.com/questions/tagged/%s' %tag]

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'answer': response.css('.answercell .post-text').extract(),
            
        }



