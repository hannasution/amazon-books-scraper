import scrapy
from AmazonBook.items import AmazonBookItem

AMAZON_URL = 'https://www.amazon.com'


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/best-sellers-books-Amazon/zgbs/books']

    def parse(self, response):

        current_category = response.xpath('//span[@class="zg_selected"]')
        category_id = response.request.url.split('/')[-1].split('?')[0]
        products = response.xpath('//li[@class="zg-item-immersion"]')

        for product in products:
            rank = product.xpath('.//span[@class="zg-badge-text"]/text()').extract_first()
            url = product.xpath('.//span/div/span/a/@href').extract_first()
            image = product.xpath('.//span/div/span/a/span/div/img/@src').extract_first()
            name = product.xpath('.//span/div/span/a/div').xpath('normalize-space(text())').extract_first()
            author = product.xpath('.//span/div/span/div[1]/*[contains(@class,"a-size-small")]/text()').extract_first()
            type = product.xpath('.//span[contains(@class,"a-color-secondary")]/text()').extract_first()
            price = product.xpath('.//span[@class="p13n-sc-price"]/text()').extract_first()
            available = product.xpath('.//*[@class="zg-item-unavailable"]').extract_first()
            book_id = url.split('/')[-1].split('?')[0]

            yield AmazonBookItem(
                id=book_id,
                rank=int(rank.replace('#', '')),
                url=AMAZON_URL + url,
                image=image,
                name=name,
                author=author,
                type=type,
                price=0 if price is None else float(price.replace('$', '')),
                category_id=parse_int(category_id),
                available=available is None
            )

        next_page = response.css('.a-last a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
        else:
            sub_category = current_category.xpath('.//parent::li/parent::ul/ul/li/a/@href').extract()
            for category_url in sub_category:
                yield scrapy.Request(category_url, callback=self.parse)


def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return 0
