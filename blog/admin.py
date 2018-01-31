# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import *



class BlogModelAdmin(admin.ModelAdmin):
    list_display = ["title", "posted_on", "updated"]
    list_filter = ["posted_on"]
    search_fields = ["title", "content"]
    class Meta:
        model= BlogPost

admin.site.register(BlogPost, BlogModelAdmin)
admin.site.register(Category)