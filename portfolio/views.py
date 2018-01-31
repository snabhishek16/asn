# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def portfolio_list(request):
    all_portfolios = Portfolio_list.objects.all()
    paginator = Paginator(all_portfolios, 6)


    page = request.GET.get('page')

    try:
        portfolios = paginator.page(page)
    except PageNotAnInteger:

        portfolios = paginator.page(1)
    except EmptyPage:

        portfolios = paginator.page(paginator.num_pages)

    context = {
        'all_portfolios': portfolios
    }

    return render(request, 'portfolio/portfolio.html', context)


def port_article(request, id=None):
    port_article = get_object_or_404(Portfolio_list, id=id)
    context = {
    'port_article' :port_article
    }
    return render(request, 'portfolio/port_article.html', context)