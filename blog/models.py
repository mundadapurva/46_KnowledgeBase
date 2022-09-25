from tkinter import CASCADE
from django.db import models

from knowledge_base.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    body = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

