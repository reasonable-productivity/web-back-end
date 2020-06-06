from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('apps.tasks.urls')),
    path('lists/', include('apps.lists.urls'))
]
