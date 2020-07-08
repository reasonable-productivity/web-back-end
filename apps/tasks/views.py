from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from apps.projects.models import Project
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())
    project = serializers.PrimaryKeyRelatedField(
            queryset=Project.objects.all(), required=False, default='')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'user',
                  'completed', 'created_at', 'updated_at',
                  'date', 'category', 'project']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
