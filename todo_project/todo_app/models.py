# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=50)
    priority=models.IntegerField()
    date=models.DateField(default=datetime.date.today,blank=True, null=True)