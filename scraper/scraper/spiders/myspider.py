import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["mydomain.com"]
    start_urls = ["http://mydomain.com/"]

    def parse(self, response):
        pass
