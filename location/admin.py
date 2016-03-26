from django.contrib import admin

from .models import *

class RegionAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Location,LocationAdmin)


