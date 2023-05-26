from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Course(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='courses', 
                              related_query_name='course')
    name=models.CharField(max_length=250)
    day=models.CharField(max_length=20)
    room=models.CharField(max_length=20)

