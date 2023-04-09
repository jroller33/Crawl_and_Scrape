# https://docs.scrapy.org/en/latest/intro/overview.html

# to run this spider, open terminal INSIDE the `quote_spider/` folder, then run `scrapy runspider quotes_spider.py -o quotes.jsonl`

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)