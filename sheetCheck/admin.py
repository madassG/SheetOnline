from django.contrib import admin
from . import models


@admin.register(models.Sheet)
class SheetAdmin(admin.ModelAdmin):
    list_display = ['sheet_format', 'columns', 'file', 'date_added']
    search_fields = ['sheet_format']
    list_filter = ('sheet_format',)


@admin.register(models.Format)
class FormatAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'desc']
    search_fields = ['code', 'name']

