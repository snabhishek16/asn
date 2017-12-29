# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Portfolio_list(models.Model):
    card_title = models.CharField(max_length=30,null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='portfolio/%y/%m/%d/',null=True)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)

    def __unicode__(self):
        return self.card_title


