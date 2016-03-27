from django.contrib import admin

# Register your models here.
from .models import Worker
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class WorkerInline(admin.TabularInline):
    model = Worker
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [
        WorkerInline,
    ]
    fields = ('username', 'password', 'first_name', 'last_name', 'email')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'role']
    class Meta:
        model = Worker

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Worker, WorkerAdmin)