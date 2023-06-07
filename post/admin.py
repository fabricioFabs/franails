from django.contrib import admin
from .models import Post, config

# Register your models here.
admin.site.register(Post)
admin.site.register(config)
