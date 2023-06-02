from django.contrib import admin
from .models import Category, Post, Services

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'image_table']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}
    
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'image_table', 'price']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Services, ServicesAdmin)
