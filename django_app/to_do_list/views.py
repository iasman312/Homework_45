from django.shortcuts import render, get_object_or_404, redirect

from .models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, id=pk)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == "GET":
        context = {'status_choices': status_choices}
        return render(request, 'task_create.html', context)
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        up_to = request.POST.get("up_to")
        if not up_to:
            up_to = None
        description = request.POST.get("description")

        task = Task.objects.create(
            title=title,
            status=status,
            up_to=up_to,
            description=description,
        )
        return redirect('task-view', pk=task.id)


def task_update_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        return render(request, 'task_update.html',
                      context={'task': task, 'status_choices': status_choices})
    elif request.method == 'POST':
        task.title = request.POST.get("title")
        task.status = request.POST.get("status")
        task.up_to = request.POST.get("up_to")
        if not task.up_to:
            task.up_to = None
        task.description = request.POST.get("description")
        task.save()
        return redirect('task-view', pk=task.id)


def task_delete_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('task-list')
