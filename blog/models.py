# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


#MVC > model view controller
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    category = models.ForeignKey(Category,null=True)
    author = models.CharField(max_length=20)
    image = models.FileField(upload_to='blog_uploads/%Y/%m/%d/')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)


    def __unicode__(self):
        return self.title


