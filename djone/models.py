#coding=utf-8
from django.db import models

class One(models.Model):
	title = models.CharField(max_length=140)
	photo = models.ImageField(upload_to = './photo',blank=True,null=True)

