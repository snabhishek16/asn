# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def posts_list (request):
    all_posts = BlogPost.objects.all()
    context = {
        'all_posts' :all_posts
    }

    return render(request,'blog/blog.html', context)

def article (request,id=None):
    article = get_object_or_404(BlogPost, id=id)
    context = {
        'article' :article
    }

    return render(request, 'blog/article.html', context)



