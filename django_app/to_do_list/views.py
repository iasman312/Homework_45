from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_create_view(request):
    if request.method == "GET":
        context = {'status_choices': status_choices}
        return render(request, 'task_create.html', context)
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        up_to = request.POST.get("up_to")
        description = request.POST.get("description")

        task = Task.objects.create(
            title=title,
            status=status,
            up_to=up_to,
            description=description,
        )
        return redirect('task-view', pk=task.id)
