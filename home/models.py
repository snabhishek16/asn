# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contact (models.Model):
    name = models.CharField (max_length=20)
    email = models.EmailField(max_length=70, blank=True,  null= True)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __unicode__(self):
        return self.name