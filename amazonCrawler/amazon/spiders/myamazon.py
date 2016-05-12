# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector        import HtmlXPathSelector



class MyamazonSpider(scrapy.Spider):
    name = "myamazon"
    allowed_domains = ["www.amazon.com"]
    start_urls = [

        "http://www.amazon.de/s/ref=sr_nr_p_n_intended_use_bro_4?fst=as%3Aoff&rh=n%3A3010075031%2Cp_n_ways_to_watch%3A7448695031%2Cp_n_entity_type%3A9739119031%2Cp_n_intended_use_browse-bin%3A3289718031%7C3289715031%7C3289719031&bbn=3010075031&ie=UTF8&qid=1462731645&rnid=3289714031"

    ]

    def parse(self, response):
        hxs     = HtmlXPathSelector(response)
        urls = hxs.select('//a[contains(@class, "s-access-detail-page")]/@href')


       # titles  = hxs.select('//h1[@id="aiv-content-title"]/text()').extract()[0]


      
        yield urls
