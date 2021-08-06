# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonBookItem(scrapy.Item):
    id = scrapy.Field()
    rank = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    type = scrapy.Field()
    price = scrapy.Field()
    category_id = scrapy.Field()
    available = scrapy.Field()


class AmazonCategoryItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    parent_category_id = scrapy.Field()
