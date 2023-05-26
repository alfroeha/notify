from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
import datetime
# Create your models here.

class CourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def get_today_courses(self, user_id):
        today = timezone.now()
        today = today.strftime('%A').lower()
        return super(CourseManager, self).filter(day=today, user_id=user_id)
    
    def get_incoming_courses(self, user_id):
        today = timezone.now() + datetime.timedelta(days=1)
        today = today.strftime('%A').lower()
        return super(CourseManager, self).filter(day=today, user_id=user_id)

class Course(models.Model):
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    )

    objects = CourseManager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses', related_query_name='course')
    name = models.CharField(max_length=250)
    day = models.CharField(max_length=20, choices=DAY_CHOICES)
    room = models.CharField(max_length=20)
