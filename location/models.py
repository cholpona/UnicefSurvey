from __future__ import unicode_literals

from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=255)


class City(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


class Location(models.Model):
    city = models.ForeignKey(City)
