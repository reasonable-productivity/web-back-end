from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from .models import List


class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())

    class Meta:
        model = List
        fields = ['name', 'description', 'user',
                  'created_at', 'updated_at']


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
