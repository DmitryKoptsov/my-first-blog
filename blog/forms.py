from django import forms

from .models import Post, Blog , Comments

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'text',)

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)

