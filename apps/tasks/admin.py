from django.contrib import admin
from .models import Task, Tag


class TaskAdmin(admin.ModelAdmin):
    fields = ('user', 'project', 'title', 'description')
    list_display = ('user', 'title', 'project', 'created_at', 'updated_at')
    # filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    fields = ('text', 'color')
    list_display = ('text', 'color')


admin.site.register(Task, TaskAdmin)
admin.site.register(Tag, TagAdmin)
