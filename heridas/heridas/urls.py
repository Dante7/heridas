from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'heridas.views.home', name='home'),
    # url(r'^heridas/', include('heridas.foo.urls')),

    url(r'^$', 'captura.views.Login'),
    url(r'^captura/', 'captura.views.Captura'),
    url(r'^generales/', 'captura.views.CapTbl1'),
    url(r'^filtros/', 'captura.views.CapTbl2'),
    url(r'^dime/', 'captura.views.CapTbl3'),
    url(r'^txp5/', 'captura.views.CapTbl4'),
    url(r'^txp6/', 'captura.views.CapTbl5'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
