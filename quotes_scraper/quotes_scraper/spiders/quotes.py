import scrapy

class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = [
		'https://quotes.toscrape.com/'
	]

	custom_settings = {
		'FEED_URI': 'quotes.json',
		'FEED_FORMAT': 'json',
		'CONCURRENT_REQUESTS': 24,
		'MEMUSAGE_LIMIT_MB': 2048,
		'MEMUSAGE_NOTIFY_MAIL': ['rvillegas@hoteltec.cl'],
		'ROBOTSTXT_OBEY': True,
		'USER_AGENT': 'Rodrigo',
		'FEED_EXPORT_ENCODING': 'utf8'
	}

	title = '//h1/a/text()'
	quotes = '//span[@class="text" and @itemprop="text"]/text()'
	authors = '//small[@class="author" and @itemprop="author"]/text()'
	top_tags = '//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()'
	next_page_btn = '//ul[@class="pager"]//li[@class="next"]/a/@href'

	def parse_only_quotes(self, response, **kwargs):
		if kwargs:
			quotes = kwargs['quotes']
			authors = kwargs['authors']
		
		quotes.extend(response.xpath(self.quotes).getall())
		authors.extend(response.xpath(self.authors).getall())

		next_page_btn = response.xpath(self.next_page_btn).get()
		if next_page_btn:
			yield response.follow(next_page_btn, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes, 'authors': authors})
		else:
			yield {
				'quotes':  list(zip(quotes, authors))
			}

	def parse(self, response):		
		title = response.xpath(self.title).get()
		quotes = response.xpath(self.quotes).getall()
		authors = response.xpath(self.authors).getall()
		top_tags = response.xpath(self.top_tags).getall()

		top = getattr(self, 'top', None)
		if top:
			top = int(top)
			top_tags = top_tags[:top]

		yield {
			'title': title,
			'top_tags': top_tags
		}

		next_page_btn = response.xpath(self.next_page_btn).get()
		if next_page_btn:
			yield response.follow(next_page_btn, callback=self.parse_only_quotes, cb_kwargs={'quotes': quotes, 'authors': authors})