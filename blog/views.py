#!/usr/bin/env python
# coding: utf-8

from blog.view.index import index
from blog.view.content import content


# Create your views here.
def view_index(request):
    return index(request)


def view_content(request):
    return content(request)
