import scrapy
from scrapy.crawler import CrawlerProcess
from items import BioItems, GenItems
import sys
import pandas as pd
import re as re

#############################################################################
## Scraping strain data (strainXassembly))#############################
#############################################################################
class BioSpider(scrapy.Spider):
    name = 'bio'
    

    def __init__(self, assemly_url=None, *args, **kwargs):
        super(BioSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'{assembly_url}']


    custom_settings = {
         'FEED_FORMAT': 'json',
         'FEED_URI': 'strainxassemblies.json'
     }

    def parse(self, response): 
        items = BioItems()

        strain_name = response.css('dd:nth-child(4)::text').extract() 
        biosampleID = response.css('dd:nth-child(6) a::text').extract() 
        submitter = response.css('dd:nth-child(10)::text').extract() 
        ## title = response.xpath("//span[@class='text']/text()").extract()
        self.link_genome['link'] = response.xpath("//h3//a/@href").extract()

        self.outputResponse['text'] = strain_name

        items['strain_name'] = strain_name
        items['biosampleID'] = biosampleID
        items['submitter'] = submitter

        yield items    

#############################################################################
## Scraping organism data (NCBI taxonomy/genome)#############################
#############################################################################

class OrgSpider(scrapy.Spider):
    name = 'org'


    def __init__(self, tx_id=None, *args, **kwargs):
        super(OrgSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id={tx_id}']

    #def show(self):
    #    print (self.start_urls)

    custom_settings = {
         'FEED_FORMAT': 'json',
         'FEED_URI': 'organism.json'
     }

    def parse(self, response):
        items = GenItems()

        tax_id = self.tx_id
        organism_name = response.css('h2 a::text').extract()
        organism_type = response.css('fieldset+ strong::text').extract()
        #representative_genome = response.css('dd:nth-child(10)::text').extract()
        #qnt_assemblies = response.css('dd:nth-child(10)::text').extract()
        #description = response.css('dd:nth-child(10)::text').extract()
        #url_evidence = response.css('dd:nth-child(10)::text').extract()

        # title = response.xpath("//span[@class='text']/text()").extract()
        #self.link_genome['link'] = response.xpath("//h3//a/@href").extract()
        #self.outputResponse['text'] = um

        items['tax_id'] = tax_id
        items['organism_name'] = organism_name
        items['organism_type'] = organism_type

        yield items    

#############################################################################

if __name__ == "__main__":
# url example https://www.ncbi.nlm.nih.gov/assembly/GCA_015033655.1

    assembly_url=sys.argv[1]
    
    outputResponse = {}
    link_genome = {}

    BioProcess = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    })
    BioProcess.crawl(BioSpider, outputResponse=outputResponse, assembly_url = assembly_url, link_genome=link_genome)
    BioProcess.start()
    

    df = pd.DataFrame.from_dict(link_genome)
    df['taxonID'] = df.link.str.extract('(\d+)')

    print('------')

    if df.iloc[0]['taxonID'] is not None:

        print(df.iloc[0]['taxonID'])

        OrgProcess = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        })
        OrgProcess.crawl(OrgSpider, tx_id = df.iloc[0]['taxonID'])
        OrgProcess.start()








