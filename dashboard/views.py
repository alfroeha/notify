from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from courses.models import Course

@login_required
def dashboard(request):
    today = Course.objects.get_today_courses(request.user.id)
    incoming = Course.objects.get_incoming_courses(request.user.id)
    return render(request, 'Dashboard.html', {'today': today, 'incoming': incoming})