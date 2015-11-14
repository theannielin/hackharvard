import scrapy


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions/33389484/advanced-css-tricks-setting-a-column-break-in-css3-multi-column-website-layout']

    #def parse(self, response):
        #for href in response.css('.question-summary h3 a::attr(href)'):
            #full_url = response.urljoin(href.extract())
            #yield scrapy.Request(full_url, callback=self.parse_question)

    def parse(self, response):
        yield {
            #'title': response.css('h1 a::text').extract()[0],
            #'votes': response.css('.question .vote-count-post::text').extract()[0],
            'answer': response.css('#answer-33668329 .post-text').extract()[0],
            #'tags': response.css('.question .post-tag::text').extract(),
            #'link': response.url,
        }