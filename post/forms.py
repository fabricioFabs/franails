from django import forms
from .models import Posts
from .models import config

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'description', 'image']

class config(forms.ModelForm):
    class Meta:
        model = config
        fields = ['title', 'description', 'image']
