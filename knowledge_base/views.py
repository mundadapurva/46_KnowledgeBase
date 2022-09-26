from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . models import *

def landing_page(request):
    return render(request, 'landing.html', {})

def home(request):
    return render(request, 'home.html', {})

def register_user(request, user):
    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        owner = request.POST['owner']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username = username).first() is not None:
            return error(request, 'User already exists. Please Login!!!')

        if password == confirm_password:
            user = User.objects.create_user(username, first_name, last_name, owner, email, password)
            user.save()
            
            return redirect('login')
    return render(request,'register_user.html', {'user': user})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return error(request, "User not found!!!")
    return render(request, 'login.html', {})

def logout(request):
    logout(request)
    return redirect('landing')

def error(request, message):
    return render(request, 'error.html', {'message':message})
