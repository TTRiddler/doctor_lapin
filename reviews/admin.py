from django.contrib import admin
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'published', 'created_date']
    list_filter = ['published', 'created_date']
    list_editable = ['published']


admin.site.register(Review, ReviewAdmin)