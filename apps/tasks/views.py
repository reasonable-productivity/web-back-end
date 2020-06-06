from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())

    class Meta:
        model = Task
        fields = ['title', 'description', 'user',
                  'created_at', 'updated_at']


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
