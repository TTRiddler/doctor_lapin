from django.contrib import admin
from seminars.models import Seminar


class SeminarAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'city', 'days_number', 'hours_number']


admin.site.register(Seminar, SeminarAdmin)