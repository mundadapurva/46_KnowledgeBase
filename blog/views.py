from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.
@login_required(login_url = 'login')
def blog(request):
    #POST
    if request.method == 'POST':
        body = request.POST['body']
        blog_post = Blog(user = request.user, body = body)
        blog_post.save()
        return render(request, 'blog.html')

    #DISPLAY
    blog_post = Blog.objects.all()

    return render(request, 'blog.html', {'blog': blog_post})