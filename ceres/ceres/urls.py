from django.conf.urls import patterns, include, url

from django.views.generic import list_detail

from ceres.pricing.models import Crop, Department, PriceReport

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ceres.views.home', name='home'),
    # url(r'^ceres/', include('ceres.foo.urls')),

    #(r'^crops/page(?P<page>[0-9]+)/$', 'object_list', dict(info_dict)),

    (r'^crops/$', list_detail.object_list, {'queryset': Crop.objects.all()}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
