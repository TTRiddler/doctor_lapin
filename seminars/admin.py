from django.contrib import admin
from seminars.models import Seminar, UpcomingSeminar


class SeminarAdmin(admin.ModelAdmin):
    list_display = ['title', 'days_number', 'hours_number']


class UpcomingSeminarAdmin(admin.ModelAdmin):
    list_display = ['seminar', 'date_start', 'date_end', 'city']


admin.site.register(Seminar, SeminarAdmin)
admin.site.register(UpcomingSeminar, UpcomingSeminarAdmin)