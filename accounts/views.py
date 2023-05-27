from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . forms import LoginForm, SignupForm

User = get_user_model()

def user_login(request):
    alert = {}
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect('dashboard')
            alert = {'message': 'Username or Password did not matched any user.', 'color': 'red'}
    else:
        form=LoginForm()
    return render(request, 'login.html', {'alert': alert})

def user_signUp(request):
    alert = {}
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                cd = form.cleaned_data
                user = User.objects.create_user(
                    username=cd['username'],
                    email=cd['email'],
                    password=cd['password']
                )
                user.first_name=cd['first_name']
                user.last_name=cd['last_name']
                user.save()
                login(request, user)
                return redirect('dashboard')
            except:
                alert = {'message': 'Username is already exists.', 'color': 'red'}
    else:
        form=SignupForm()
    return render(request, 'signUp.html', {'alert': alert})

def user_logout(request):
    logout(request)
    return redirect('login')
        
