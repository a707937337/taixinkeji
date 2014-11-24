#coding=utf8
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^users/', 'service.main.ssh'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'gaga.views.login'),
    url(r'^regist/$', 'gaga.views.regist'),
    url(r'^index/$', 'gaga.views.index'),
    url(r'^logout/$', 'gaga.views.logout'),

   url(r'^index/testresource/$', 'gaga.views.testresource'),
)
urlpatterns += patterns('gaga.views', #gaga.views为公共对象，patterns返回的对象可以相加

         url(r'^index/samba/$', 'samba'),




)