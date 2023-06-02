from django.urls import path
from . import views
from post .models import Post

urlpatterns = [
    path('', views.inicio, name='homebase'),
    path('post-create', views.post_create, name='post-create'),
    path('paginas/post-list.html', views.post_list, name='post-list'),
    path('post-detail/<int:id>/', views.post_detail, name='post-detail'),
    path('post-delete/<int:id>/', views.post_delete, name='post-delete'),
]