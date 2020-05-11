from datetime import datetime as dt
import scrapy
import json
import itertools

class HomeSpider(scrapy.spiders.Spider):
    name = "home-spider"
    allowed_domains = ['eatigo.com']
    start_urls = [
        'https://eatigo.com/sg/singapore/en/view-all-a-z'
    ]

    def parse(self, response):
        initial_state = response.css('div[id*=alphabet_letter_]')
        links = []
        for alphabet in initial_state:
            for item in alphabet.css('a'):
                Slug = item.attrib['href']
                Name = item.css('div::text').get()
                links.append({"slug":Slug, "name": Name})
        yield {"slugs": links}



