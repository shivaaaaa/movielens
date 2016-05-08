# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector        import HtmlXPathSelector


class MyamazonSpider(scrapy.Spider):
    name = "myamazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = [

        "http://www.amazon.de/dp/B00MQ9QDOU"

    ]

    def parse(self, response):
        hxs     = HtmlXPathSelector(response)
        titles  = hxs.select('//h1[@id="aiv-content-title"]/text()').extract()[0]

        print("titles=", titles)
        yield titles
