from django.db import models
from knowledge_base.models import User


# Create your models here.
class Tutorial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=10)
    video = models.FileField(upload_to='static/video',null=True, verbose_name='')
    date_uploaded = models.DateTimeField(auto_now_add=True)
