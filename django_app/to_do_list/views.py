from django.shortcuts import render, get_object_or_404, redirect

from .models import Task, status_choices
from .forms import TaskForm


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        context = {'status_choices': status_choices, 'form': form}
        return render(request, 'task_create.html', context)
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task(
                title=form.cleaned_data.get('title'),
                status=form.cleaned_data.get('status'),
                up_to=form.cleaned_data.get('up_to'),
                description=form.cleaned_data.get('description')
            )
            task.save()
            return redirect('task-view', pk=task.id)

        return render(request, 'task_create.html', context={'form': form})


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'status': task.status,
            'up_to': task.up_to,
            'description': task.description
        })
        return render(request, 'task_update.html', context={'form': form,
                                                               'task': task})

    elif request.method == 'POST':
        form = TaskForm(
            data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get("title")
            task.status = form.cleaned_data.get("status")
            task.up_to = form.cleaned_data.get("up_to")
            task.description = form.cleaned_data.get("description")
            task.save()
            return redirect('article-view',
                            pk=task.id)

        return render(request, 'task_create.html', context={'form': form,
                                                               'task': task})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task-list')
