from django.urls import path, include
from rest_framework_nested import routers
from .views import ProjectViewSet, ProjectTaskViewSet

router = routers.SimpleRouter()
router.register(r'', ProjectViewSet)

project_router = routers.NestedSimpleRouter(router, r'', lookup='list')
project_router.register('tasks', ProjectTaskViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
]
