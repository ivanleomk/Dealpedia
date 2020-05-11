from datetime import datetime as dt
import scrapy
import json
import itertools
import googlemaps
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BurpleSpider(scrapy.spiders.Spider):
    name='burple-spider'
    allowed_domains = ['burpple.com']

    def start_requests(self):
        with open('eatigo.json') as json_file:
            data = json.loads(json_file.read())
        self.crawls = data
        urls = []
        for item in data:
            slug = item['url']
            name = '+'.join(slug.split('/')[-1].split('-')[:-1])
            url = "https://www.burpple.com/search/sg?city_code=sg&ll=&q={}".format(name)
            urls.append(url)
        start_urls = urls[0]
        import pdb
        pbb.set_trace()
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self,response):
        links = response.css('div[class*=feed-item]').xpath('a').attrib['href']
        for link in links:
            yield scrapy.Request(link,callback=parse_location)
    

    def parse_location(self,response):
        import pdb
        pdb.set_trace()
