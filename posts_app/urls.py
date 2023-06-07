from django.urls import path
from . import views
from post .models import Post

urlpatterns = [
    path('', views.inicio, name='homebase'),
    path('home', views.home, name= 'home'),
    path('post-create', views.post_create, name='post-create'),
    path('post-list', views.post_list, name='post-list'),
    path('post-config', views.post_config, name='post-config'),
    path('post-detail/<int:id>/', views.post_detail, name='post-detail'),
    path('post-delete/<int:id>/', views.post_delete, name='post-delete'),
    path('post-update/<int:id>/', views.post_update, name='post-update'),
    

]