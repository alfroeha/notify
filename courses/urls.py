from django.urls import path
from . views import courses, course

urlpatterns = [
  path('', courses, name='courses'),
  path('<int:id>', course, name='course')
]