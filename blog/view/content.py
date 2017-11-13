#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render
from blog.models import Content, Articles


def content(request):
    id = request.GET.get('id')
    article = Articles.objects.get(id=id)
    content = Content.objects.get(id=id)
    return render(request, 'blog/content.html', {'content': content, 'article': article})
