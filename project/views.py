from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def projectCollab(request):
    return render(request, 'project_collab.html', {})