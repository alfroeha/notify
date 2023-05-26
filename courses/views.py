from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Course

# Create your views here.
@login_required
def courses(request):
  courses = Course.objects.filter(user_id=request.user.id)
  today = Course.objects.get_today_courses(request.user.id)
  incoming = Course.objects.get_incoming_courses(request.user.id)
  return render(request, 'Courses.html', {'courses': courses, 'today': today, 'incoming': incoming})