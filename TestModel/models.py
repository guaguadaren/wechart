# models.py
from django.db import models


class Test(models.Model):
    u_name = models.CharField(max_length=200)
    u_pwd = models.CharField(max_length=200)