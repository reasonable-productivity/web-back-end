from django.urls import path, include
from rest_framework_nested import routers
from .views import ListViewSet, ListItemViewSet

router = routers.SimpleRouter()
router.register(r'', ListViewSet)

lists_router = routers.NestedSimpleRouter(router, r'', lookup='list')
lists_router.register(r'list-items', ListItemViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(lists_router.urls)),
]
