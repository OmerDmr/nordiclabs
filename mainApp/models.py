from django.db import models
import uuid
from django.urls import reverse


class Products(models.Model):
    prdId = models.CharField(max_length=12,unique=True,null=False, verbose_name='Product ID')
    used = models.IntegerField(default=0)


