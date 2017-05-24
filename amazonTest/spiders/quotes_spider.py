import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books?_encoding=UTF8&pg=1',
    ]

    def parse(self, response):
        item = response.css('div.zg_itemImmersion')
        # rank = response.css('div.zg_itemImmersion div.zg_rankDiv span.zg_rankNumber::text').extract()

        for i in item:
            yield {
            'Rank': i.css('div.zg_rankDiv span.zg_rankNumber::text').extract_first(),
            'Title': i.css('div.a-section a.a-link-normal div.p13n-sc-truncated-hyphen::text').extract_first(),
            'Author': i.css('div.a-section a.a-link-child::text').extract_first(),
            'Price': i.css('div.a-section div.a-row span.a-size-base span.p13n-sc-price::text').extract_first()
            }

        next_page = response.css('li.zg_page a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

# response.css(div.zg_itemImmersion)
#         rank = response.css('div.rankDiv span.zg_rankNumber::text').extract()

# rank number
# response.css('span.zg_rankNumber::text').extract()


# book title
# response.css('div.a-section a.a-link-normal div.p13n-sc-truncated-hyphen::text').extract()
# response.css('div.p13n-sc-truncated-hyphen::text').extract()

# author
# response.css('div.a-section a.a-link-child::text').extract()
# response.css('a.a-link-child::text').extract()

# prices
# response.css('div.a-section div.a-row span.a-size-base span.p13n-sc-price::text').extract()
# rank_price = response.css('span.p13n-sc-price::text').extract()pan.p13n-sc-price::text').extract()
# def top_twenty(items):
#     for i in range(21):
#         print items[i]
# top_twenty(rank_price)
