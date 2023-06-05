from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from courses.models import Course
from todos.models import Todo

@login_required
def dashboard(request):
    Todos_todo = Todo.objects.filter(status='todo', user_id=request.user.id)
    Todos_in_progress = Todo.objects.filter(status='in_progress', user_id=request.user.id)
    Todos_completed = Todo.objects.filter(status='completed', user_id=request.user.id)

    today = Course.objects.get_today_courses(request.user.id)
    incoming = Course.objects.get_incoming_courses(request.user.id)
    tasks = {'todo': Todos_todo, 'in_progress': Todos_in_progress, 'completed': Todos_completed}
    return render(request, 'Dashboard.html', {'today': today, 'incoming': incoming, 'tasks': tasks})