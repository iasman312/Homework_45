from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'up_to']
    list_filter = ['title']
    search_fields = ['title', 'status']
    fields = ['id', 'title', 'status', 'up_to', 'description']
    readonly_fields = ['up_to', 'id']


admin.site.register(Task, TaskAdmin)