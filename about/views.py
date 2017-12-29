# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404


# Create your views here.

def about_me (request):
    if request.method == 'GET':
        return render(request, 'about/about.html')