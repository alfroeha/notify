from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . models import Course
from . forms import CourseForm

# Create your views here.
@login_required
def courses(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      cleaned_data = form.cleaned_data
      course = Course(user_id=request.user.id, name=cleaned_data['name'], room=cleaned_data['room'], day=cleaned_data['day'])
      course.save()
      return redirect('courses')
  courses = Course.objects.filter(user_id=request.user.id)
  today = Course.objects.get_today_courses(request.user.id)
  incoming = Course.objects.get_incoming_courses(request.user.id)
  return render(request, 'Courses.html', {'courses': courses, 'today': today, 'incoming': incoming})

@login_required
@csrf_exempt
def course(request, id):
  course = get_object_or_404(Course, id=id)
  if request.method == 'DELETE':
    course.delete()
    return JsonResponse({'error': None})
  elif request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      cleaned_data = form.cleaned_data
      course.name = cleaned_data['name']
      course.room = cleaned_data['room']
      course.day = cleaned_data['day']
      course.save()
    return redirect('courses')
  data = {
    'id': course.id,
    'name': course.name,
    'room': course.room,
    'day': course.day
  }
  return JsonResponse(data)