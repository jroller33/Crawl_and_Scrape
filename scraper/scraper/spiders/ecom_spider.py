import scrapy


# class MyspiderSpider(scrapy.Spider):
#     name = "myspider"
#     allowed_domains = ["mydomain.com"]
#     start_urls = ["http://mydomain.com/"]

#     def parse(self, response):
#         pass

from scraper.items import Product

class EcomSpider(scrapy.Spider):
    name = 'ecom_spider'
    allowed_domains = ['clever-lichterman-044f16.netlify.app']
    start_urls = ['https://clever-lichterman-044f16.netlify.app/products/taba-cream.1/']

    def parse(self, response):
        item = Product()
        item['product_url'] = response.url
        item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
        item['title'] = response.xpath('//section[1]//h2/text()').get()
        item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
        return item