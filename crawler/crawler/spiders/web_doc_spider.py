import scrapy
from scrapy.crawler import CrawlerProcess
import os


class WebDocumentSpider(scrapy.Spider):
    name = 'web_document_spider'
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'DEPTH_LIMIT': 3,
        'DOWNLOAD_DELAY': 5
    }

    def __init__(self, start_url='http://quotes.toscrape.com', limit_pages=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]
        self.limit_pages = limit_pages
        self.pages_downloaded = 0

    def parse(self, response):
        if self.pages_downloaded < self.limit_pages:
            self.pages_downloaded += 1
            page_name = response.url.split("/")[-2] + '.html'
            dir_path = 'downloaded_pages'
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, page_name)

            with open(file_path, 'wb') as file:
                file.write(response.body)
            self.log(f'Saved {file_path}')

            for link in response.css('a::attr(href)'):
                yield response.follow(link, callback=self.parse)
