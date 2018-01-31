# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .forms import *
# Create your views here.

def home_page(request):
    if request.method == 'GET':
        return render(request, 'home/index.html')


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            print 'saved'
            return render(request, 'home/index.html')
        else:
            print 'error sent'
            return render(request, 'home/index.html', {'form' : form, 'contact' : True })
    else:
        print 'nothing'
        return render(request, 'home/index.html', { 'contact' : True })