from django import forms
from post .models import Post

class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']
