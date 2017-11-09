#!/usr/bin/env python
# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_index, name='index'),
    url(r'^content/$', views.view_content, name='content')
]
