from pydoc import describe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import ProjectCollab

# Create your views here.

@login_required(login_url = 'login')
def projectCollab(request):
    #POST
    if request.method == 'POST':
        desciption = request.POST['description']
        techstack = request.POST['techstack']
        contributors = request.POST['contributors']
        project_post = ProjectCollab(user = request.user, desciption = desciption, techstack = techstack, contributors = contributors)
        project_post.save()
        return render(request, 'project_collab.html')

    #DISPLAY
    project_post = ProjectCollab.objects.all()

    #FILTER OBJECTS
    # projectPast = ProjectCollab.objects.get(department='IT')
    # projectUpcoming = ProjectCollab.objects.get(department='CS')
    # projectRunning = ProjectCollab.objects.get(department='EnTC')
    return render(request, 'project_collab.html', {'project': project_post})