from django.db import models

from knowledge_base.models import User

# Create your models here.
class ProjectCollab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    techStack = models.CharField(max_length=50)
    contributos = models.CharField(max_length=100)
    date_uploaded = models.DateTimeField(auto_now_add=True)