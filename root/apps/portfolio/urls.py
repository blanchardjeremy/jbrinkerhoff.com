from django.conf.urls import *
from portfolio.views import *

urlpatterns = patterns('',
    url(r'^work/$',     WorkView.as_view(),  name='work'),
    url(r'^$',          HomeView.as_view(),  name='home'),


    url(r'^temp/$',    TempView.as_view(),  name='temp'),
)