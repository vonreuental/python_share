# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import TslaItem


class Model3Spider(CrawlSpider):
    name = 'model3'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series-s40012/5346.html']
    rules = (
        Rule(LinkExtractor(allow=r"https://car.autohome.com.cn/pic/series-s40012/5346.+"), callback="parse_page",
             follow=True),
    )

    def parse_page(self, response):
        category = response.xpath("//div[@class='uibox']/div/text()").get()
        scrs = response.xpath("//div[contains(@class, 'uibox-con')]/ul/li//img/@src").getall()
        scrs = list(map(lambda x: response.urljoin(x.replace('240x180_0_q95_c42', '1024x0_1_q95')), scrs))
        print(scrs)
        yield TslaItem(category=category, image_urls=scrs)
