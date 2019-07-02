from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(SystemConfig)
class SystemConfigAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'label', 'type', 'key', 'value')
    list_filter = ('type',)
    list_editable = ('type', 'key')
    search_fields = ('key',)


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    search_fields = ('name', 'parent_id')
    list_display = ('id', 'name', 'url', 'parent_id', 'sort')
    list_per_page = 10


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    search_fields = ('name', 'contact')
    list_filter = ('type',)
    list_display = ('id', 'name', 'url', 'sort', 'type', 'contact', 'create_date', 'update_date')
    list_per_page = 10
