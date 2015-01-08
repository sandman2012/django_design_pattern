from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_design_pattern.views.home', name='home'),
    # url(r'^django_design_pattern/', include('django_design_pattern.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^news/', include(urls)),
    url(r'^news/', include('app.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))

)
