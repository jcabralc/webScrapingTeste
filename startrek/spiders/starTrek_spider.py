from scrapy import Spider, http
from scrapy.selector import Selector

from startrek.StarTrekItems import StarTrekItem


class starTrekSpider(Spider):
    # some attributes
    accomulated=[]

    name = "StarTrek"
    allowed_domains = ["startrek.com"]
    start_urls = ["http://www.startrek.com" ]

    def parse(self, response):
        all_links = Selector(response).xpath('*//a/@href').extract()

        for link in all_links:
            print(link)
            item = StarTrekItem()
            item['url'] = link
            yield item
