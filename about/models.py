# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Self_Intro (models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.name