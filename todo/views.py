from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)

    tasks = Task.objects.all()
    return render(request, 'todo.html', {'tasks': tasks})

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('/')