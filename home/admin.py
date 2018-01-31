# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["name", "sent_on"]
    list_filter = ["name"]
    search_fields = ["name", "email", "message"]
    class Meta:
        model= Contact

admin.site.register(Contact, ContactModelAdmin)