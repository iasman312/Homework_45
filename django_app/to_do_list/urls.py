from django.urls import path
from .views import index_view, task_view, task_create_view, delete_task

urlpatterns = [
    path('', index_view, name='task-list'),
    path('tasks/add/', task_create_view, name='task-add'),
    path('task/<int:pk>/', task_view, name='task-view'),
    path('delete_task/<int:pk>/', delete_task, name='task-delete'),
]