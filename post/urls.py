from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts_app.urls')),
    path('ckeditor/', include('ckeditor_uloader.urls')),
] * static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
