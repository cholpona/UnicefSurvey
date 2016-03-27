from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from surveys.models import City

# Create your models here.

ROLES_CHOICES = (
    ('admin', 'Admin'),
    ('worker', 'Worker'),
)

class Worker(models.Model):
    user = models.OneToOneField(User)
    city = models.ForeignKey(City, null=True)
    role = models.CharField(max_length=120, null=True, blank=True, choices=ROLES_CHOICES)

    def __unicode__(self):
        return self.user.username
