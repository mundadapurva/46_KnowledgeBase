from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.

@login_required(login_url = 'login')
def resources(request):
    #POST
    if request.method == 'POST':
        department = request.POST['department']
        body = request.POST['body']
        resource_post = Resources(user = request.user, department = department, body = body)
        resource_post.save()
        return render(request, 'resources.html')

    #DISPLAY
    resource_post = Resources.objects.all()

    #FILTER OBJECTS
    # resourceIT = Resources.objects.get(department='IT')
    # resourceComp = Resources.objects.get(department='CS')
    # resourceEntc = Resources.objects.get(department='EnTC')
    # resourceOthers = Resources.objects.get(department='Others')

    return render(request, 'resources.html', {'resource': resource_post})