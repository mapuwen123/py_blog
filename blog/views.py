#!/usr/bin/env python
# coding: utf-8

from blog.view.content import content
from blog.view.index import index
from blog.view.contact import contact
from blog.view.about import about


# Create your views here.
def view_index(request):
    return index(request)


def view_content(request):
    return content(request)


def view_contact(request):
    return contact(request)


def view_about(request):
    return about(request)
