from django.shortcuts import render
from user_auth import forms
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


def signup(request):
    form = forms.SignupForm()

    if request.method=='POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_auth:signin'))
    return render(request, 'auth_template/signup.html', context={'form':form})


def signin(request):
    loginform = AuthenticationForm()

    if request.method=='POST':
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('user_auth:profile'))

    return render(request, 'auth_template/login.html', context={'loginform':loginform})


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('content:blog_list'))

@login_required
def profile(request):
    return render(request, 'auth_template/user_profile.html',context={})
# Create your views here.
