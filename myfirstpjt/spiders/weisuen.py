# -*- coding: utf-8 -*-
import scrapy
from myfirstpjt.items import MyfirstpjtItem


class WeisuenSpider(scrapy.Spider):
    name = 'weisuen'
    allowed_domains = ['sina.com.cn']

    start_urls = ['http://mil.news.sina.com.cn/jssd/2017-09-09/doc-ifykuffc4576787.shtml',
                  'http://mil.news.sina.com.cn/jssd/2017-09-09/doc-ifykusey6035938.shtml',
                  'http://mil.news.sina.com.cn/jssd/2017-09-09/doc-ifykusey6175905.shtml',]

    def parse(self, response):
        item = MyfirstpjtItem()
        item["urlname"] = response.xpath("//a[@target='_blank']/text()")
        print(item["urlname"])
        pass
