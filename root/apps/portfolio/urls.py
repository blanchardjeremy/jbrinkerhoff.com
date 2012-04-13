from django.conf.urls import *
from portfolio.views import *

urlpatterns = patterns('',
    url(r'^acorn/$',    InnerView.as_view(),  name='inner'),
    url(r'^$',          HomeView.as_view(),  name='home'),


    url(r'^flickr/$',    FlickrCacheResetView.as_view(),  name='flickr_cache_reset'),
    url(r'^help/$',     HelpView.as_view(), name='help')
)