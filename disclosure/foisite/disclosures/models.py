from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class DjangoDisclosure(models.Model):
#    department = models.ForeignKey(Department)
    department = models.CharField(max_length=200)
    source = models.CharField(max_length=500)
#    disclosure_date = models.DateTimeField('date disclosed')
    disclosure_date = models.DateTimeField()
#    spider_date = models.DateTimeField('date spidered')
    ref_number = models.CharField(max_length=30)
    description = models.TextField()
    release_type = models.CharField(max_length=500)
    how_to_access = models.TextField()

    def was_disclosed_recently(self):
        return self.disclosure_date >= timezone.now() - datetime.timedelta(days=1)
    
    def date(self):
        return self.disclosure_date.strftime('%d %m %Y')

    def __unicode__(self):
        return self.description[:200]


    
