from django.shortcuts import render

from .models import Task, status_choices


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', context={'tasks': tasks})


def task_view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'task_view.html', context={'task': task})


def task_create_view(request):
    if request.method == "GET":
        context = {'status_choices': status_choices}
        return render(request, 'task_create.html', context)
    elif request.method == "POST":
        title = request.POST.get("title")
        status = request.POST.get("status")
        up_to = request.POST.get("up_to")

        task = Task.objects.create(
            title=title,
            status=status,
            up_to=up_to
        )

        return render(request, 'task_view.html', context={'task': task})

