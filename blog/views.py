#!/usr/bin/env python
# coding: utf-8

from blog.view.content import content
from blog.view.index import index


# Create your views here.
def view_index(request):
    return index(request)


def view_content(request):
    return content(request)
