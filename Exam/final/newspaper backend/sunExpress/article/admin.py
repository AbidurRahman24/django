from django.contrib import admin
from . import models
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline','body', 'category','editor_name','publishing_time']
    def editor_name(self,obj):
        return obj.editor.user.first_name
    
admin.site.register(models.Article, ArticleAdmin)
