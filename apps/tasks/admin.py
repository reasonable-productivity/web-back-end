from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('user', 'project', 'title', 'description')
    list_display = ('user', 'title', 'project', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)
