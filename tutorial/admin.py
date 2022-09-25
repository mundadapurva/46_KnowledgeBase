from django.contrib import admin

from tutorial.models import Tutorial
from . models import *

# Register your models here.
admin.site.register(Tutorial)