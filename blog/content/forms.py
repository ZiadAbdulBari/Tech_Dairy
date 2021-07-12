from django import forms
from django.forms import fields
from content.models import BlogWrite

class BlogWriteForm(forms.ModelForm):
    class Meta:
        model = BlogWrite
        fields = ('title','short_description', 'blog_content', 'blog_image')