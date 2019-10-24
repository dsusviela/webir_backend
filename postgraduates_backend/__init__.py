import scrapy
from .scrapy_service.postgrados.spiders.ort_spider import OrtSpider
from .scrapy_service.postgrados.spiders.um_spider import UmSpider
from scrapy.crawler import CrawlerProcess

def fetch_data():
    process = CrawlerProcess()
    process.crawl(UmSpider)
    process.crawl(OrtSpider)
    process.start()
    print('Spiders finished')

def startup():
    fetch_data()
    # populate_database()

startup()