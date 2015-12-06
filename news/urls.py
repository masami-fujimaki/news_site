# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^category/([a-z].*)/$', views.category, name='category'),
)

