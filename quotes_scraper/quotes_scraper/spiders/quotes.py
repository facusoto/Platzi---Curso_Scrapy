import scrapy

# Título = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //span[@class="tag-item"]/a[@class="tag"]/text()
# next page button = '//ul[@class="pager"]//li[@class="next"]/a/@href'

class QuotesSpider(scrapy.Spider):
    # name es el nombre unico con el scrapy se va referir al spider dentro del proyect.
    # name debe ser unico.
    name = 'quotes'
    # Defiimos una lista de url a las cuales les vamos a realizar las peticiones http.
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]
    custom_settings = {
        'FEED_URI': 'quotes.json',
        'FEED_FORMAT': 'json'
    }
    # definir el metodo parse el cual nos sirve para analizar un archivo y extraer informacion valiosa a partir de el.
    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_ten_tags = response.xpath('//span[@class="tag-item"]/a[@class="tag"]/text()').getall()

        yield {
            'title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)