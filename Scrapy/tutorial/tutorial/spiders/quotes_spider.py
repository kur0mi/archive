#!coding: utf-8
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        for href in response.css('li.next a'):
            yield response.follow(href, callback=self.parse)
        for href in response.css('.author+a'):
            yield response.follow(href, callback=self.parse_author)

    def parse_author(self, response):
        yield {
            'author-title': response.css('h3.author-title::text').extract_first(),
            'author-born-date': response.css('.author-born-date::text').extract_first(),
            'author-description': response.css('.author-description::text').extract_first(),
        }

