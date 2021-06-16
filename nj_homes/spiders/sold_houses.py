import scrapy
from scrapy.loader import ItemLoader
from ..utils import NJ_SOLD_URL, cookie_parser, parse_new_url
from ..items import NjHomesItem
import json

class SoldHousesSpider(scrapy.Spider):
    name = 'sold_houses'
    allowed_domains = ['www.zillow.com']

    def start_requests(self):
        yield scrapy.Request(
            url=NJ_SOLD_URL,
            callback=self.parse,
            cookies=cookie_parser(),
            meta={
                'currentPage' : 1
            }
        )

    def parse(self, response):
        current_page = response.meta['currentPage']
        json_res = json.loads(response.body)
        houses = json_res.get('cat1').get('searchResults').get('listResults')
        for house in houses:
            loader = ItemLoader(item=NjHomesItem())
            loader.add_value('address', house.get('address'))
            loader.add_value('zip', house.get('addressZipcode'))
            loader.add_value('bed', house.get('beds'))
            loader.add_value('bath', house.get('baths'))
            loader.add_value('area', house.get('area'))
            loader.add_value('soldDate', house.get('variableData').get('text'))
            loader.add_value('soldPrice', house.get('unformattedPrice'))
            loader.add_value('zestimate', house.get('zestimate'))
            yield loader.load_item()

            
            if current_page < 2250:
                yield scrapy.Request(
                    url = parse_new_url(NJ_SOLD_URL, pg_num=current_page+1),
                    callback=self.parse,
                    cookies=cookie_parser(),
                    meta={
                        'currentPage' : current_page+1
                    }
                )
            
