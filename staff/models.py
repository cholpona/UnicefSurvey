from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Worker(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=120, null=True, blank=True)
