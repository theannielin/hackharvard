# marky.py
# Authors: {Annie Lin, Joanne Koong}
# Date: {December 7, 2015}
# Emails: {annielin@college.harvard.edu, joannekoong@college.harvard.edu}
# ----------------
# Our methods for scraping StackOverflow.

import scrapy
import sys


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow' 
    list = []

    def __init__(self, tag=None, *args, **kwargs):
        super(StackOverflowSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://stackoverflow.com/questions/tagged/%s?sort=frequent&pageSize=15' % tag.lower()]

    def parse(self, response):
        # Get the answers using the correct attribute
        for href in response.css('.summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        # Return tag-related answers as JSON
        new_answer = response.css('.answercell .post-text').extract()
        if len(new_answer) != 0:
            yield {
                'answer': new_answer,
            }



