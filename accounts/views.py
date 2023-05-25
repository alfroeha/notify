from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required

User = get_user_model()

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password=cd['password'])
    else:
        form=LoginForm()
    return render(request, 'login.html')

def user_signUp(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password']
            )
            user.first_name=cd['first_name']
            user.last_name=cd['last_name']
            user.save()
            return HttpResponse('<h1>Signup Successful</h1>')
    else:
        form=SignupForm()
    return render(request, 'signUp.html')

def user_logout():
    redirect('login')
        
