from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from disclosure.items import DisclosureItem

import html2text

class HealthSpider(BaseSpider):
    name = "health"
    allowed_domains = ["http://www.health.nsw.gov.au/"]
    start_urls = ["http://www.health.nsw.gov.au/gipaa/disclosures.asp"]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        rows = hxs.select('//tr/td')
        
        rows_list = []
        for row in rows:
            row = html2text.html2text(row.extract())
            print row
            rows_list.append(row[:-2])

        ref_nums = rows.select('p[starts-with(.,"PA")]/text()').extract()

        items = []
        for ref_num in ref_nums:
            print ref_num
            i = rows_list.index(ref_num)
            item = DisclosureItem()
            item['department'] = unicode('Department of Health')
            item['source'] = unicode("http://www.health.nsw.gov.au/gipaa/disclosures.asp")
            item['ref_number'] = ref_num
            item['disclosure_date'] = rows_list[i+1]
            item['description'] = rows_list[i+2] 
            item['release_type'] = rows_list[i+3]
            item['how_to_access'] = rows_list[i+4]
            items.append(item)
            #print item #for testing uncomment this line and comment out next line
            item.save()
        return items

#filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
