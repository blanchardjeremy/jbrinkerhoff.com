from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from mainsite.views import *
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

admin.autodiscover()
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)


handler500 = 'mainsite.views.error500'
handler404 = 'mainsite.views.error404'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    (r'', include('portfolio.urls')),

)


if not settings.DEBUG or settings.DJANGO_SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )