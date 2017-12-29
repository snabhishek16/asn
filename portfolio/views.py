# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *

from django.shortcuts import render, get_object_or_404

# Create your views here.
def portfolio_list(request):
    all_portfolios = Portfolio_list.objects.all()
    context = {
        'all_portfolios': all_portfolios
    }
    return render(request, 'portfolio/portfolio.html', context)


def port_article(request, id=None):
    port_article = get_object_or_404(Portfolio_list, id=id)
    context = {
    'port_article' :port_article
    }
    return render(request, 'portfolio/port_article.html', context)