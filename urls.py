from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^test/', direct_to_template, {
        'template': 'test.html',
    }),
    (r'^paste/$', direct_to_template, {
        'template': 'test_paste/test_change.html',
    }),
)
urlpatterns += staticfiles_urlpatterns()
