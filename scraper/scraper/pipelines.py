# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import re

class ScraperPipeline:
    def process_item(self, item, spider):
        return item


class PriceValidatorPipeline:
	def process_item(self, item, spider):

		price = item.get('price')

		if price is not None:
			price = re.sub("[^0-9\.]", "", price)

			if price:
				# Convert string to float
				price = float(price)

				# Validate price
				if price < 10 or price > 100:
					price = None
			else:
				price = None

		if price is not None :
			
			# Set normalised price
			item['price'] = price;

			return item
		else:
			return None