from django.urls import path
from content import views

app_name = 'content'

urlpatterns = [
    path('',views.blog_list, name='blog_list'),
    path('blog-post/', views.blogWrite, name='blog_write'),
    path('blog-read/<str:slug>/', views.blogRead, name='blog_open'),
    path('my-bolg/', views.my_blog, name='my_blog'),
    path('blog-edit/<str:slug>', views.blog_edit, name='blog_edit'),
    
]