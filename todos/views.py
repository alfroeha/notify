from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required

@login_required
def todo(request):
    Todos_todo = Todo.objects.filter(status='To Do')
    Todos_in_progress = Todo.objects.filter(status='In Progress')
    Todos_completed = Todo.objects.filter(status='Completed')
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('')

    context = {
        'Todos_todo': Todos_todo,
        'Todos_in_progress': Todos_in_progress,
        'Todos_completed': Todos_completed,
        'form': form
    }
    return render(request, 'Todos.html', context)

@login_required
def update_status(request, pk, status):
    Todo = Todo.objects.get(id=pk)
    Todo.status = status
    Todo.save()
    return redirect('')

@login_required
def delete_Todo(request, pk):
    Todo = Todo.objects.get(id=pk)
    Todo.delete()
    return redirect('')
