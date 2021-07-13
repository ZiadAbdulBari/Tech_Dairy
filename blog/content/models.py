from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField
from django.forms.fields import SlugField
from hitcount.models import HitCount,HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation

class BlogWrite(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=155, verbose_name="Title")
    short_description = models.TextField(default=None)
    slug = models.SlugField(max_length=155, unique=True)
    blog_content = models.TextField()
    blog_image = models.ImageField(upload_to='blog_img', blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',related_query_name='hit_count_generic_relation')
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
 
# Create your models here.
