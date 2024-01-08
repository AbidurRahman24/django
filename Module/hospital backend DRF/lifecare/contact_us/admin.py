from django.contrib import admin
from .models import ContactUs
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']
admin.site.register(ContactUs,ContactAdmin)