from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Post
=======
from .models import Category, Post, Services
>>>>>>> 5592fd6 (initial commit)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'image_table']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}

<<<<<<< HEAD
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
=======
class PostServices(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at', 'image_table']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Services, PostServices)

>>>>>>> 5592fd6 (initial commit)
