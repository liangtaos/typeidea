# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.

from django.http import HttpResponse, Http404

from .models import Post, Tag



def post_list(request, category_id=None, tag_id=None):
	queryset = Post.objects.all()
	page = request.GET.get('page', 1)
	page_size = 4
	try:
		page = int(page)
	except TypeError:
		page = 1
	if category_id:
		# 分类页面
		queryset = queryset.filter(category_id=category_id)
	elif tag_id:
		# 标签页面
		try:
			tag = Tag.objects.get(id=tag_id)
		except Tag.DoesNotExist:
			queryset = []
		else:
			queryset = tag.post_set.all()

#		queryset = queryset.filter(tag_id=tag_id)
	paginator = Paginator(queryset, page_size)	
	try:
		posts = paginator.page(page)
	except EmptyPage:
		posts = paginator.get(paginator.num_pages)
	context = {
		'posts':posts
	}
	return render(request, 'blog/list.html', context=context)
#	return HttpResponse('test')


def post_detail(request, pk=None):
   
	try:
		post = Post.objects.get(pk=pk)
	except Post.DoesNotExist:
		raise Http404('Poll dose not exist!')


	context ={
		'post': post
	}
	return render(request, 'blog/detail.html', context=context)
