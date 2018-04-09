# coding:utf-8

from .base import * #NOQA



DEBUG = True


DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.mysql',
 		'NAME': 'typeidea',
 		'USER': 'root',
 		'PASSWORD': 'g19860817',
 		'HOST': '127.0.0.1',
 		'PORT': '3306',
	}
}
