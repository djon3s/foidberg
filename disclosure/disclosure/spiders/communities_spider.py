from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from disclosure.items import DisclosureItem

import html2text

class CommunitiesSpider(BaseSpider):
    name = "communities"
    allowed_domains = ["http://www.communities.nsw.gov.au/"]
    start_urls = ["http://www.communities.nsw.gov.au/gipainfo/gipa_disclosurelog.asp"]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        rows = hxs.select("//table[1]/tr/td")

        rows_list = []
        for row in rows:
            row = html2text.html2text(row.extract())
            print row
            rows_list.append(row[:-2])

        ref_nums = rows.select('p[starts-with(.,"2") and contains(.,"/")]/text()').extract()
 
        #rows_list = rows.select('p/text()').extract()
        items = []
        for ref_num in ref_nums:
            i = rows_list.index(ref_num)
            item = DisclosureItem()
            item['department'] = unicode('Office of Communities')
            item['source'] = unicode("http://www.communities.nsw.gov.au/gipainfo/gipa_disclosurelog.asp")
            item['ref_number'] = ref_num
            item['disclosure_date'] = rows_list[i+1]
            item['description'] = rows_list[i+3]
            item['how_to_access'] = rows_list[i+4]
            item['release_type'] = rows_list[i+2]
            items.append(item)
            #print item
            item.save()
        return items

#filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
