from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'description')
    list_display = ('user', 'title', 'created_at', 'updated_at')


admin.site.register(Project, ProjectAdmin)
