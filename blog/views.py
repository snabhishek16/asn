# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib import quote_plus
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# Master
def posts_list (request):
    all_posts = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-publish')
    latest_blogs = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-id')[:4]
    cat = Category.objects.all()

    paginator = Paginator(all_posts, 4)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:

        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    context = {
        'all_posts' :blogs,
        'latest_blogs' :latest_blogs,
        'cat' :cat,
    }

    return render(request,'blog/blog.html', context)


def article (request,id=None):
    article = get_object_or_404(BlogPost, id=id)
    latest_blogs = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-id')[:4]
    cat = Category.objects.all()
    share_string = quote_plus(article.content)
    context = {
        'article' :article,
        'latest_blogs' :latest_blogs,
        'cat': cat,
        'share_string' :share_string,
    }

    return render(request, 'blog/article.html', context)


def search_blog (request):
    all_posts = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-publish')
    latest_blogs = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-id')[:4]
    cat = Category.objects.all()


    query = request.GET.get("q")
    if query:
        all_posts = all_posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)).distinct()

    paginator = Paginator(all_posts, 4)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:

        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    context = {
        'all_posts' :blogs,
        'latest_blogs' :latest_blogs,
        'cat' :cat,
    }

    return render(request,'blog/blog.html', context)



def search_category(request, name=None):
    all_posts = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-publish')
    latest_blogs = BlogPost.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by('-id')[:4]
    cat=Category.objects.all()
    this_cat = get_object_or_404(cat, name=name)
    posts_all = BlogPost.objects.filter(category=this_cat.id)

    paginator = Paginator(posts_all, 4)

    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:

        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    context = {
        'all_posts': blogs,
        'posts_all' : posts_all,
        'latest_blogs': latest_blogs,
        'cat' : cat,
        'current_category': name,
    }


    return render(request, 'blog/blog.html', context)





