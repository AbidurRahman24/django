from django.contrib import admin
from . import models
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }

class FlowerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'created_by']
    search_fields = ['title', 'description', 'category']

admin.site.register(models.FlowerCategory, CategoryAdmin)
admin.site.register(models.Flower,FlowerAdmin)
admin.site.register(models.Order)