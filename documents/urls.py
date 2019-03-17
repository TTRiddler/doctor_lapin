from django.urls import path
from documents import views

urlpatterns = [
    path('all/', views.all_documents, name='all_documents'),
]