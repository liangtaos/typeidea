# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Post



def post_list(request, category_id=None, tag_id=None):
	queryset = Post.objects.all()
	print dir(queryset)
	if category_id:
		# 分类页面
		queryset = queryset.object.filter(category_id=category_id)
	elif tag_id:
		# 标签页面
        
		queryset = queryset.object.filter(tag_id=tag_id)
	
	context = {
		'posts':queryset
	}
	return render(request, 'blog/list.html', context=context)
#	return HttpResponse('test')


def post_detail(request, post_id=None):
	context ={
		'name': 'study'
	}
	return render(request, 'blog/detail.html', context=context)
