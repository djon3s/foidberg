from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from disclosure.items import DisclosureItem

import html2text

import dateutil.parser

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
            #item['disclosure_date'] = rows_list[i+1]
            a,b,c = rows_list[i+1].split(' ')
            print a, b, c
            if b[0] =='S':
                rows_list[i+1]= ''.join([a, ' Sep ',  c])
            elif b[0] == 'N':
                rows_list[i+1]= ''.join([a, ' Nov ',  c])
            print rows_list[i+1]
            print a ,b ,c
            item['disclosure_date'] = dateutil.parser.parse(rows_list[i+1]).date().strftime("%Y-%m-%d %H:%M:%S")
            item['description'] = rows_list[i+3]
            item['how_to_access'] = rows_list[i+4]
            item['release_type'] = rows_list[i+2]
            items.append(item)
            #print item
            item.save()
        return items

#filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
