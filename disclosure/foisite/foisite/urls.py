from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #remove in production
from foisite.feeds import LatestDisclosures#, LatestDisclosuresByDepartment

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
    'latest': LatestDisclosures,
    #'department': LatestDisclosuresByDepartment,
}

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'foisite.views.home', name='home'),
    #to fix I removed include()
                       #url(r'^', ''disclosures.views.index'),
                       #url(r'^disclosures/static/(?P<resource_path>\d+)$', 'static'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed', {'feed_dict' : feeds}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += staticfiles_urlpatterns()
