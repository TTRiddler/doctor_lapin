from django.urls import path
from seminars import views

urlpatterns = [
    path('all/', views.all_seminars, name='all_seminars'),
    path('upcoming/', views.upcoming_seminars, name='upcoming_seminars'),
    path('<seminar_id>/', views.seminar_detail, name='seminar_detail'),
]