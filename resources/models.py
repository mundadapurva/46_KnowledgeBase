from django.db import models

from knowledge_base.models import User

# Create your models here.
class Resources(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, default='Other')
    body = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)