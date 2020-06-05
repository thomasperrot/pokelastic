import scrapy


class Pokemon(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    types = scrapy.Field()
    description = scrapy.Field()
