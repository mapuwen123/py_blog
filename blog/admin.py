#!/usr/bin/env python
# coding: utf-8

from django.contrib import admin
from .models import Articles, Content

# Register your models here.
admin.site.register(Articles)


@admin.register(Content)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'content',
    )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/kindeditor/kindeditor-all.js',
            'js/kindeditor/lang/lang.zh_CN.js',
            'js/kindeditor/config.js',
        )
