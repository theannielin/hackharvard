import scrapy
import sys


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow' 
    list = []
    def __init__(self, tag=None, *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://stackoverflow.com/questions/tagged/%s?sort=frequent&pageSize=15' % tag.lower()]

    def parse(self, response):
        for href in response.css('.summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        new_answer = response.css('.answercell .post-text').extract()
        if len(new_answer) != 0:
            yield {
                'answer': new_answer,
            }



