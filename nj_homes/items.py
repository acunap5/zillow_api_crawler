import scrapy
from itemloaders.processors import TakeFirst

class NjHomesItem(scrapy.Item):
    address = scrapy.Field(
        output_processor = TakeFirst()
    )
    zip = scrapy.Field(
        output_processor = TakeFirst()

    )
    bed = scrapy.Field(
        output_processor = TakeFirst()

    )
    bath = scrapy.Field(
        output_processor = TakeFirst()

    )
    area = scrapy.Field(
        output_processor = TakeFirst()
    )
    soldDate = scrapy.Field(
        output_processor = TakeFirst()
    )
    soldPrice = scrapy.Field(
        output_processor = TakeFirst()
    )
    zestimate = scrapy.Field(
        output_processor = TakeFirst()
    )

    pass
