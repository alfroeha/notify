from django.urls import path
from . views import todos, todo

urlpatterns = [
  path('', todos, name='todos'),
  path('<int:id>', todo, name='todo'),
]