__author__ = 'atomixsystem'
from django.conf.urls import patterns, url
from app import views



# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name='home')

)

