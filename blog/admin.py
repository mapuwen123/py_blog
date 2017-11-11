#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin

from .models import Articles, Content, Contact

# Register your models here.
admin.site.register(Articles)
admin.site.register(Content)
admin.site.register(Contact)
