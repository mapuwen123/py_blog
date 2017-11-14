#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin

from .models import Articles, Content, Contact


# Register your models here.
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    # 列表展示字段
    list_display = (
        'id',
        'title',
        'date',
    )
    # 每页展示条数
    list_per_page = 25
    # 排序
    ordering = (
        '-date',
    )

    search_fields = ('title',)  # 搜索字段


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
    list_per_page = 25
    ordering = (
        '-id',
    )

    search_fields = ('title',)  # 搜索字段


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
    )
    list_per_page = 25
    ordering = (
        '-id',
    )

    search_fields = ('name',)  # 搜索字段
