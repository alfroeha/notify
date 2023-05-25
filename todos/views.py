from django.shortcuts import render

# Create your views here.
def todos(request):
  return render(request, 'Todos.html')