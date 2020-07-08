from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, ProjectTaskViewSet

router = routers.DefaultRouter()
router.register(r'', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('{pk}/get_project_tasks', include(router.urls)),
]

# from rest_framework_nested import routers
# from .views import ProjectViewSet, ProjectTaskViewSet

# router = routers.SimpleRouter()
# router.register(r'', ProjectViewSet)

# project_router = routers.NestedSimpleRouter(router, r'', lookup='project')
# project_router.register('', ProjectTaskViewSet, basename='project')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('get_project_tasks', include(project_router.urls)),
# ]
