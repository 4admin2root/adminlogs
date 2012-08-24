from django.conf.urls.defaults import patterns, include, url
from adminlogs.views import hello,current_datetime,current_datetime_t
from adminlogs.rgraph import linechart7 
from adminlogs.rgraph_line3 import linechart3 
from adminlogs.views import hours_ahead
from adminlogs.views import main_frame
from adminlogs.views import matplot
from adminlogs.views import matplotpic
import settings
import os.path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminlogs.views.home', name='home'),
    # url(r'^adminlogs/', include('mydjangotest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    ('^linechart7/$', linechart7),
    ('^linechart3/$', linechart3),
    (r'^libraries/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    ('^timet/$', current_datetime_t),
    ('^matplot/$', matplot),
    ('^$',main_frame),
    ('^img/matplotpic.png/$', matplotpic),
)
