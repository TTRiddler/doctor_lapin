from django.urls import path
from articles import views

urlpatterns = [
    path('all/', views.all_articles, name='all_articles'),
    path('<article_id>/', views.article_detail, name='article_detail'),
]