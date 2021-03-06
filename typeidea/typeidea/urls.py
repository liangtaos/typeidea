# coding:utf-8

from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site

#from blog.views import post_list,post_detail
#from config.views import links
from blog.views import IndexView, CategoryView, TagView, PostView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$',CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^post/(?P<pk>\d+)/$',PostView.as_view(), name='detail'),
    #url(r'^links/$', links),


    url(r'^super_admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
