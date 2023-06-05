from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todos(request):
    Todos_todo = Todo.objects.filter(status='todo', user_id=request.user.id)
    Todos_in_progress = Todo.objects.filter(status='in_progress', user_id=request.user.id)
    Todos_completed = Todo.objects.filter(status='completed', user_id=request.user.id)

    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            todo = Todo(user_id=request.user.id, title=cleaned_data['title'], description=cleaned_data['description'], status=cleaned_data['status'])
            todo.save()
        return redirect('todos')

    context = {
        'tasks': {
            'todo': Todos_todo,
            'in_progress': Todos_in_progress,
            'completed': Todos_completed,
        }
    }
    return render(request, 'Todos.html', context)

@login_required
@csrf_exempt
def todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'DELETE':
        todo.delete()
        return True
    elif request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            todo.title = cleaned_data['title']
            todo.description = cleaned_data['description']
            todo.status = cleaned_data['status']
            todo.save()
        return redirect('todos')
    data = {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'status': todo.status
    }
    return JsonResponse(data)
