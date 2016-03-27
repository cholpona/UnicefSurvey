from django.contrib import admin

from .models import *


class RegionAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('title','region','lat','lng')
    search_fields = ('title',)
    list_filter = ('region',)


admin.site.register(City, CityAdmin)
admin.site.register(Region, RegionAdmin)
