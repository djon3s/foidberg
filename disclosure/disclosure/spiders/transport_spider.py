from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from disclosure.items import DisclosureItem

import html2text

import dateutil.parser

class TransportSpider(BaseSpider):
    name = "transport"
    allowed_domains = ["http://www.transport.nsw.gov.au"]
    start_urls = ["http://www.transport.nsw.gov.au/content/disclosure-log"]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        rows = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/table/thead/tr/td')

        rows_list = []
        for row in rows:
            row = html2text.html2text(row.extract())
            print row
            rows_list.append(row[:-2])

        ref_nums = rows.select('p[starts-with(.,"1") and contains(.,"-")]/text()').extract()
 
        #rows_list = rows.select('p/text()').extract()
        items = []
        for ref_num in ref_nums:
            i = rows_list.index(ref_num)
            item = DisclosureItem()
            item['department'] = unicode('Department of Transport')
            item['source'] = unicode("http://www.transport.nsw.gov.au/content/disclosure-log")
            item['ref_number'] = ref_num
            #hackish cludge
            a,b,c = rows_list[i+1].split(' ')
            print a, b, c
            if b[0] =='S':
                rows_list[i+1]= ''.join([a, ' Sep ',  c])
            elif b[0] == 'N':
                rows_list[i+1]= ''.join([a, ' Nov ',  c])
            print rows_list[i+1]
            print a ,b ,c
            item['disclosure_date'] = dateutil.parser.parse(rows_list[i+1]).date().strftime("%Y-%m-%d %H:%M:%S")
            item['description'] = rows_list[i+2]
            item['how_to_access'] = "gipa@transport.nsw.gov.au" if "Email or written request to the address above." in rows_list[i+3] else rows_list[i+3]
            item['release_type'] = 'NA'
            items.append(item)
            item.save()
        return items

#filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
