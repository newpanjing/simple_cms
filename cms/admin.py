from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'alias')
    list_display = ('id', 'name', 'alias', 'sort')
    list_per_page = 10


@admin.register(Article)
class ArticeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'cover_display', 'title', 'hits', 'create_date', 'update_date')
    search_fields = ('title',)
    list_filter = ('category',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_per_page = 10

    list_display = ('id', 'sort', 'article', 'cover_display')
