from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from knowledge_base import models

# Create your views here.
@login_required
def tutorial(request):
    videos = Tutorial.objects.all()
    return render(request, 'tutorial.html', {'videos' : videos})