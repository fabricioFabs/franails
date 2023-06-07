# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
# Create your models here.


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        ordering = ['id']



class config (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'config'
        verbose_name_plural = 'config'
        ordering = ['id']
        
        