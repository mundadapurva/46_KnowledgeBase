from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=20) #teacher or student?
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=True)
    
class Tutorial(models.Model):
    user = models.ForeignKey(User)
    owner = models.CharField(max_length=10)
    video = models.FileField(upload_to='Tutorials',null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    user = models.ForeignKey(User)
    body = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

class Resources(models.Model):
    user = models.ForeignKey(User)
    department = models.CharField(max_length=100, default='Other')
    body = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

class ProjectCollab(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=200)
    techStack = models.CharField(max_length=50)
    contributos = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)

