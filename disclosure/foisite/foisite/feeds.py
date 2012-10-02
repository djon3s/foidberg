from django.contrib.syndication.views import Feed
from disclosures.models import DjangoDisclosure
#import pdb
#pdb.set_trace()

class LatestDisclosures(Feed):
    title = 'Latest NSW FOI disclosures'
    link = 'some_website_bla.com'
    description = 'New entries added when NSW Government department updates their disclosure logs'
    
    def items(self):
        return DjangoDisclosure.objects.order_by('-disclosure_date')[:10]
