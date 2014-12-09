#coding=utf8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^users/', 'service.main.ssh'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gaga.views.my_login'),
    url(r'^regist/$', 'gaga.views.regist'),
    url(r'^index/$', 'gaga.views.index'),
    url(r'^logout/$', 'gaga.views.logout'),

   url(r'^index/testresource/$', 'gaga.views.testresource'),
   url(r'^index/testresource/(?P<tab>\d)/$', 'gaga.views.changetab'),
)
urlpatterns += patterns('gaga.views', #gaga.views为公共对象，patterns返回的对象可以相加

         url(r'^index/samba/$', 'samba'),
         url(r'^index/json/$', 'json_data'),
         url(r'^upload/$', 'upload'),
         url(r'error/$', 'noreal'),
         url(r'webSSH/$', 'term'),
)
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,
        }),
)
