from django.urls import path
from .views import index_view, task_view, task_create_view, task_update_view

urlpatterns = [
    path('', index_view, name='task-list'),
    path('add/', task_create_view, name='task-add'),
    path('<int:pk>/', task_view, name='task-view'),
    path('<int:pk>/edit/', task_update_view, name='task-update')
]