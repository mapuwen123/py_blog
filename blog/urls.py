#!/usr/bin/env python
# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.view_index, name='index'),
    url(r'^content/$', views.view_content, name='content'),
    url(r'^contact/$', views.view_contact, name='contact'),
    url(r'^about/$', views.view_about, name='about'),
    url(r'^regist/$', views.view_regist, name='regist'),
    url(r'^login/$', views.view_login, name='login'),
]
