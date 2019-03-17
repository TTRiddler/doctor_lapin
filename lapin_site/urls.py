from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site


admin.site.site_header = 'Сайт доктора Алексея Лапина' 


urlpatterns = [
    path('admin/filebrowser/', site.urls),
    path('imagefit/', include('imagefit.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('seminars/', include('seminars.urls')),
    path('articles/', include('articles.urls')),
    path('documents/', include('documents.urls')),
    path('contacts/', include('contacts.urls')),
    path('reviews/', include('reviews.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
