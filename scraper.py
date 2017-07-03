import scrapy

class ChonSpider(scrapy.Spider):
	name = "Chon_scrape"
	start_urls = ['http://4chan.org/co/']

def parse(self, response):
	SET_SELECTOR = 'img'
	for chon in response.css(SET_SELECTOR):

		NAME_SELECTOR = 'span.dateTime'
		yield {
			'date': chon.css(NAME_SELECTOR).extract_first(),
		}
