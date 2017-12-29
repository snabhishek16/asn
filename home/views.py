# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
# Create your views here.

def home_page(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')
