import scrapy


class QuitesSpides(scrapy.Spider):
    name = "quotes"

    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        self.logger.info("hello this is my first spider")
        pass
