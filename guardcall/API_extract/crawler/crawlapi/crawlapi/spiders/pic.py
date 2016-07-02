# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PicSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["theguardian.com"]
    start_urls = ['https://www.theguardian.com/world']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('.*',), )),
    )

    def parse(self, response):
        pass
