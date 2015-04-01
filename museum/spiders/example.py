from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from museum.items import Website
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import *

class MuseumSpider(CrawlSpider):
    name = "museum"
    allowed_domains = ["guggenheim.org"]
    start_urls = [
        "http://www.guggenheim.org/new-york/collections/collection-online/artwork-types/195198/"]

    rules = (
        Rule(
            SgmlLinkExtractor(
            allow_domains=("guggenheim.org",),
            restrict_xpaths=('////div[@class="ui"]',)),
            callback='parse_page', follow=True
        ),
    )

    def parse_page(self, response):
        hxs = HtmlXPathSelector(response) # The XPath selector
        titles = hxs.select('///div[@class="artwork-title"]')
        for titles in titles:
            item = Website()
            item['link'] = titles.select('a/@href').extract()
            url = 'http://www.guggenheim.org{}'.format(''.join(item['link']))
            yield Request(url=url, meta={'item': item}, callback=self.parse_item_page)


    def parse_item_page(self, response):
        hxs = HtmlXPathSelector(response)     
        item = response.meta['item']
        item['imageurl'] = hxs.select ('///img[@class="art-huge"]/@src').extract()
        item['artistname'] = hxs.select('///div[@class="artwork-details essay"]/p[1]/a/text()').extract()
        item['biographicaldata'] = hxs.select ('///div[@class="artwork-details essay"]/p[1]/text()').extract()
        item['title'] = hxs.select('///div[@class="artwork-details essay"]/p[2]/text()').extract()
        item['date'] = hxs.select ('///div[@class="artwork-details essay"]/p[3]/a/text()').extract()
        item['medium'] = hxs.select ('///div[@class="artwork-details essay"]/p[4]/text()').extract()
        item['dimensions'] = hxs.select ('///div[@class="artwork-details essay"]/p[5]/text()').extract()
        item['creditline'] = hxs.select('///div[@class="artwork-details essay"]/p[6]/text()').extract()
        item['accession'] = hxs.select('///div[@class="artwork-details essay"]/p[7]/text()').extract()
        item['copyright'] = hxs.select('///div[@class="artwork-details essay"]/p[8]/text()').extract()
        item['artworktype'] = hxs.select ('///div[@class="artwork-details essay"]/p[9]/a/text()').extract()
        return item

