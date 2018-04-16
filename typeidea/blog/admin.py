# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Post, Category, Tag
# Register your models here.@
from typeidea.custom_site import custom_site
from .adminforms import PostAdminForm

@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
	form = PostAdminForm
	list_display = [
		'title', 'category','status_show','owner',
		'created_time' ,'operator',
	] # 在文章页面显示的内容
	#list_display_links = [ 'category', 'status']  # 让分类和状态可点
	search_fields = ['title', 'category__name', 'owner__username']
	list_filter = ['category', 'owner']  # 过滤器
#	save_on_top =True 
#a	show_full_result_count = True
#	date_hierarchy = 'created_time'
#	list_editable = ('title',)  # 在admin页面可编辑
# 编辑页面
	def operator(self, obj):
		return format_html(
			"<a href={}> 编辑 </a>",
			reverse('cus_admin:blog_post_change',args=(obj.id,))	
		)
	#operator.allow_tags=True
	operator.short_description = '操作'
	

	save_on_top = True  # 把保存按钮放到顶部
	#fields = (
#		('category', 'title'),
#		'content',
#	)        # 布局
#	exclude = ('owner',)  # 不展示的和fields相反
#	fieldsets = (
#		(
#			'基础配置',{ 'fields':(('category', 'title'), 'content') }
#		),
#		(
#			'高级配置', {'classes':('collapse', 'addon'),'fields':('tags',)}
#		),
#
#	)
	

@admin.register(Tag, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time')

@admin.register(Category, site=custom_site)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time')
#admin.site.register(Post, PostAdmin)
#admin.site.register(Tag, site=custom_site)
#admin.site.register(Category, site=custom_site)

