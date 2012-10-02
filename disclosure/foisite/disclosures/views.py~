# Create your views here.
from django.http import HttpResponse
from disclosures.models import DjangoDisclosure
from django.template import Context, loader

def index(request):
    latest_disclosure_list = DjangoDisclosure.objects.all().order_by('-disclosure_date')[:10]
    t = loader.get_template('index.html')
    c = Context({
            'latest_disclosure_list' : latest_disclosure_list,
            })
    #output = ' '.join(['<ul>'+d.description[:200]+'<b> Date </b>'+d.disclosure_date.strftime('%d %m %Y')+'</ul>' for d in latest_disclosure_list])
    #return HttpResponse("<ul><b>Hello world: here are the 10 latest disclosures from the NSW gov...</b></ul>" + output)
    return HttpResponse(t.render(c))

