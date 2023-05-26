from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    STATUS_CHOICES=(
        ('todo', 'To do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Complemeted'),
    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='id_user')
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=500)
    status = models.CharField(max_length=20,
                                choices=STATUS_CHOICES,
                                default='todo')
