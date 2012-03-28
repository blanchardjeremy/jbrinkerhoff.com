from django.conf.urls import *
from portfolio.views import *

urlpatterns = patterns('',
    url(r'^inner/$',    InnerView.as_view(),  name='inner'),
    url(r'^$',          HomeView.as_view(),  name='home'),
)