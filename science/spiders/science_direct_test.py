import scrapy
import json
import re
from ..items import ScienceItem

class QuoteSpider(scrapy.Spider):
    name = 'sciencedirect'
    with open("volume_list.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        items = ScienceItem()
        all_article_list = response.css('.issue-item')
        for paper in all_article_list:
            article_name = paper.css('.issue-item__title a::text').extract()[0]
            article_link = paper.css('.issue-item__title a::attr(href)').extract()[0]
            items['article_name'] = article_name
            items['article_link'] = 'https://arc.aiaa.org' + article_link
            yield items
        # yield {
        #         'key': keyword_test
        # }
