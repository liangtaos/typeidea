# coding:utf-8

from django.contrib.admin.sites import AdminSite

class CustomSite(AdminSite):
	site_header = 'Blog后台'
	site_title = '后台'
	index_title = '首页'
	

custom_site = CustomSite(name='cus_admin')
