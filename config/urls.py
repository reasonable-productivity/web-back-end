from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('lists/', include('apps.lists.urls')),
    path('projects/', include('apps.projects.urls'))
]
