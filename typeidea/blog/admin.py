# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Category, Tag
# Register your models here.@



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	pass



class CategoryAdmin(admin.ModelAdmin):
	pass


class TagAdmin(admin.ModelAdmin):
	pass
#admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)

