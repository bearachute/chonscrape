#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy


class ChonSpider(scrapy.Spider):

    name = 'Chon_scrape'
    start_urls = ['http://boards.4chan.org/co/']

    def parse(self, response):
        SET_SELECTOR = 'span.subject'
        for chons in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'post op'
        yield {'text': chons.css(NAME_SELECTOR).extract_first()}
