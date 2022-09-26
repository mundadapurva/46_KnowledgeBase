from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *
from knowledge_base import models
from . models import *

# Create your views here.
@login_required
def tutorial(request):
    #POST
    if request.method == 'POST':
        owner = request.POST['owner']
        video = request.POST['video']
        tutorial_post = Tutorial(user = request.user, owner = owner, video = video)
        tutorial_post.save()
        return render(request, 'tutorial.html')

    #DISPLAY
    tutorial_post = Tutorial.objects.all()

    #FILTER OBJECTS
    # tutorialTeacher = Tutorial.objects.get(owner='Teacher')
    # tutorialStudent = Tutorial.objects.get(owner='Student')


    return render(request, 'tutorial.html', {'videos' : tutorial_post})