from django.urls import path
from .views import (
    index_view,
    task_view,
    task_create_view,
    task_update_view,
    task_delete_view,
    tasks_delete_all_view
)

urlpatterns = [
    path('', index_view, name='task-list'),
    path('add/', task_create_view, name='task-add'),
    path('<int:pk>/', task_view, name='task-view'),
    path('<int:pk>/update/', task_update_view, name='task-update'),
    path('<int:pk>/delete/', task_delete_view, name='task-delete'),
    path('delete_all/', tasks_delete_all_view,
         name='tasks-delete-all')
]