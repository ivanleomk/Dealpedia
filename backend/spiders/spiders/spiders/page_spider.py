from datetime import datetime as dt
import scrapy
import json
import itertools
import googlemaps

class PageSpider(scrapy.spiders.Spider):
    name='page-spider'
    allowed_domains = ['eatigo.com']

    def __init__(self, category=None, *args, **kwargs):
        super(PageSpider, self).__init__(*args, **kwargs)
        with open('slugs.json') as json_file:
            data = json.loads(json_file.read())
        self.gmaps = googlemaps.Client(key='AIzaSyAoF5kcm9n_gUCTLMj_9SHZeapsecOfWQo')
        slugs = [item['slug'] for item in data[0]['slugs']]
        self.start_urls = [
            'https://eatigo.com{}'.format(item) for item in slugs
        ]

    def parse(self, response):
        menu_section = response.css('div[class*=eatigo-restaurant__tab]').css('div[class*=menu]')
        menu_items = self.parse_menu_discounts(menu_section)

        discount_divs = response.css('section[class*=discount-wrapper]').xpath('//div//label//span/..//..')
        discount_slots = self.parse_discounts(discount_divs)

        about_section = response.css('div[class*=eatigo-restaurant__tab]').css('div[class*=about]')
        information = self.parse_about_section(about_section)

        review_section = response.css('div[class*=eatigo-restaurant__tab]').css('div[class*=feedback]')
        reviews = self.parse_ratings(review_section)


        yield {
            "url":response.url[18:],
            "discounted_items": menu_items,
            "discounted_timeslots": discount_slots,
            "information": information,
            "reviews": reviews
        }

    def parse_ratings(self,review_section):
        customer_ratings = review_section.xpath('*')[0].xpath('.//div/text()')[2:]
        main_rating = customer_ratings[0].get()
        others = [item.get() for item in customer_ratings[1:]]
        ratings = {}
        for i in range(5,0,-1):
            ratings[i] = others[5-i]
        comments =  review_section.xpath('*')[1].xpath('*').xpath('.//div//div/text()/../..')[1:]
        comments_cleaned = []
        for comment in comments:
            name = comment.xpath('*')[0].xpath('./text()').getall()[0]
            date = comment.xpath('*')[1].xpath('./text()').getall()[0]
            remarks = comment.xpath('*')[2].xpath('./text()').getall()[0]
            comments_cleaned.append({
                "name":name,
                "date":date,
                "remarks":remarks
            })

        return {
            'main-rating': main_rating,
            'breakdown': ratings,
            'comments':comments_cleaned
        }


    def parse_discounts(self,discount_div):
        discounts = []
        for div in discount_div:
            prices = ' '.join(
                list(itertools.chain.from_iterable([item.getall() for item in div.xpath('.//span/text()')])))
            discounts.append(prices.split('-'))
        return [item for item in discounts if item!=['']]

    def parse_menu_discounts(self,menu_div):
        menu = [item.xpath('.//div/text()').getall() for item in menu_div.css('div[class*=dt-row]')][1:]
        return [item for item in menu if item[1]>item[2]]

    def parse_about_section(self,about_div):
        divs = about_div.xpath('*')
        description = divs[0].xpath('.//p/text()').get()

        restaurant_bio = divs[0].xpath('*')[1:].xpath('.//h4|span')

        curr = 0
        prev = 0
        restaurant_bio_cleaned = {}
        while curr<len(restaurant_bio):
            if restaurant_bio[curr].extract().strip()[:3] == "<h4":
                if curr == 0 and prev == 0:
                    curr+=1
                    continue
                restaurant_bio_cleaned[restaurant_bio[prev].xpath('./text()').extract()[0]] = [item.xpath('./text()').extract()[0] for item in restaurant_bio[prev+1:curr]]

                prev = curr
            curr+=1

        restaurant_opening_hours = divs[2].xpath('*')[1].xpath('*').xpath('*')

        restaurant_opening_hours_cleaned = {}
        for index, table_row in enumerate(restaurant_opening_hours):

            table_row_nodes = [item.xpath('./text()').extract() for item in table_row.xpath('*')]
            if index == 0 and table_row_nodes[2][0] == "Lunch":
                continue
            restaurant_opening_hours_cleaned[table_row_nodes[0][0]] = table_row_nodes[1:]
        
        lat_long = divs[1].xpath('*')[1].xpath('.//a').attrib['href'].split('/')[-1].split('=')[-1].split(',')
        lat_long_formatted = (float(lat_long[0]),float(lat_long[1]))
        restaurant_address = self.encode_using_lat_long(lat_long_formatted)
        returnObj =  {
            "bio" : description,
            "facilities": restaurant_bio_cleaned,
            "opening_hours": restaurant_opening_hours_cleaned,
            "restaurant_address": restaurant_address
        }

        return returnObj

        # prev = 0
        # curr = 0
        # other-info-grouping = []
        # while curr<len(other-info):
        #     if other-info[curr].extract().strip()[:3]=="<h4":
        #         if start == 0 and curr == 0:
        #             pass
        #         else:
        #             other-info-grouping.append(other-info[prev:curr])
        #             start = curr+1
        #     curr+=1
    
    def encode_using_lat_long(self,lat_long):
        data = self.gmaps.reverse_geocode(lat_long)
        postal_code = data[0]['address_components'][-1]['long_name']
        formatted_address = data[0]['formatted_address']
        neighbourhood = data[0]['address_components'][2]['long_name']

        address = {
            "postal_code":postal_code,
            "address": formatted_address,
            "neighbourhood": neighbourhood,
            "lat-long": lat_long
        }

        return address






