from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def landing_page(request):
    return render(request, 'landing.html', {})

def home(request):
    return render(request, 'home.html', {})

def register_user(request, user):
    return render(request,'register_user.html', {'user': user})

def login(request):
    return render(request, 'login.html', {})

def logout(request):
    return render(request, 'logout.html', {})


