import scrapy
from AmazonBook.items import AmazonCategoryItem


class CategorySpider(scrapy.Spider):
    name = 'category'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/best-sellers-books-Amazon/zgbs/books']

    def parse(self, response):

        active_category = response.xpath('//span[@class="zg_selected"]')

        current_category_id = response.request.url.split('/')[-1].split('?')[0]
        category_id = parse_int(current_category_id)

        yield AmazonCategoryItem(
            id=category_id,
            name=active_category.xpath('normalize-space(text())').extract_first(),
            parent_category_id=response.meta['parent_id'] if 'parent_id' in response.meta.keys() else 0
        )

        sub_category = active_category.xpath('.//parent::li/parent::ul/ul/li/a/@href').extract()
        for category_url in sub_category:
            yield scrapy.Request(category_url, callback=self.parse, meta={'parent_id': category_id})


def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return 0
