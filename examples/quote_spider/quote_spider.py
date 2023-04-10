# https://docs.scrapy.org/en/latest/intro/tutorial.html

# to run this spider, open terminal INSIDE the `quote_spider/` folder, then run `scrapy runspider quotes_spider.py -o quotes.jsonl`
# `quotes.jsonl` in this folder is the log generated from running the spider.

# you can also run the spider from the top-level of the directory, using `scrapy crawl quotes`

from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'             # identifies the spider, must be unique within a project
    
    def start_requests(self):   # must return iterable of Requests (list of req's or make a function)
        urls = [                            # starting list of URLs for the spider
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):       # the response object from the request is passed into the parse method
        # handles the response downloaded for each request, usually extracts scraped data as dictionaries
        
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
        
        
        
    # def parse(self, response):                 
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'author': quote.xpath('span/small/text()').get(),
    #             'text': quote.css('span.text::text').get(),
    #         }

    #     next_page = response.css('li.next a::attr("href")').get()
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)