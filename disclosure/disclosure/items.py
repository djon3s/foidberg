# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib_exp.djangoitem import DjangoItem
from disclosures.models import DjangoDisclosure
"""
class DisclosureItem(Item):
    # define the fields for your item here like:
    # name = Field()
    department = Field()
    source = Field()
    ref_number = Field()
    decision_date = Field()
    description = Field()
    release_type = Field()
    how_to_access = Field()
    pass
"""
class DisclosureItem(DjangoItem):
    # define the fields for your item here like:
    # name = Field()
    django_model = DjangoDisclosure
"""
    department = Field()
    source = Field()
    ref_number = Field()
    decision_date = Field()
    description = Field()
    release_type = Field()
    how_to_access = Field()
    pass
"""
