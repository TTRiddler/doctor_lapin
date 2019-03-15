from django.contrib import admin
from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created_date']
    list_filter = ['published', 'created_date']
    list_editable = ['published']


admin.site.register(Article, ArticleAdmin)