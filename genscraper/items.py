from typing import Text
import scrapy


class BioItems(scrapy.Item): 
    strain_name = scrapy.Field()
    biosampleID = scrapy.Field()
    submitter = scrapy.Field()
    pass


class GenItems(scrapy.Item):
    tax_id = scrapy.Field()
    organism_name = scrapy.Field()
    organism_type = scrapy.Field()
    pass