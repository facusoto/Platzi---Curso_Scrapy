import scrapy

"""
Title = //h1/a/text()
Quotes = //span[@class="text" and @itemprop="text"]/text()
Top Ten Tags = //div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()
Next = //ul[@class="pager"]//li[@class="next"]/a/@href
"""


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/page/1/"
    ]
    custom_settings = {
        "FEED_URI": "quotes.json",
        "FEED_FORMAT": "json"
    }

    def parse_only_quotes(self, response, **kwargs):
        new_quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()
        kwargs["quotes"].extend(new_quotes)

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(
                next_page_button_link,
                callback=self.parse_only_quotes,
                cb_kwargs=kwargs
            )
        else:
            yield kwargs

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()

        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()

        tags = response.xpath(
            '//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(
                next_page_button_link,
                callback=self.parse_only_quotes,
                cb_kwargs={
                    "title": title,
                    "quotes": quotes,
                    "top_ten_tags": tags,
                }
            )