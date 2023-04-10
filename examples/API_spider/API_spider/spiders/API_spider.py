# this is a version of the quote_spider that uses the site's API and query parameters. It requests every page to scrape every quote from the whole site, in a more efficient way

import scrapy
import json


class QuoteSpider(scrapy.Spider):           
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    page = 1
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):              # response is a JSON object
        data = json.loads(response.text)    # you can use `data` like a Python dictionary
        
        for quote in data["quotes"]:
            yield {"quote": quote["text"]}
        
        if data["has_next"]:          # this checks if there's a next page
            self.page += 1           # increments the query parameter at the end of the URL
            url = f"https://quotes.toscrape.com/api/quotes?page={self.page}"    
            yield scrapy.Request(url=url, callback=self.parse)