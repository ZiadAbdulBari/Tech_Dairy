from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
from django.forms.fields import SlugField

class BlogWrite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=155, verbose_name="Title")
    short_description = models.TextField(default=None)
    slug = models.SlugField(max_length=155, unique=True)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_img', blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
 
# Create your models here.
