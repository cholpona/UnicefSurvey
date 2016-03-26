# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % (self.title)


    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class City(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s, %s" % (self.title, self.region.title)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
