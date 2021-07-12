from django.urls import path
from user_auth import views

app_name = 'user_auth'

urlpatterns = [
    path('profile/',views.profile, name='profile'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
]