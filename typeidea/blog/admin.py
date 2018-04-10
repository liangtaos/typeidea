# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag
# Register your models here.@



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = [
		'title', 'category',
		'created_time',
	]


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time')

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'status', 'created_time')
#admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

