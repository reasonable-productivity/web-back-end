from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from .models import List, ListItem


class ListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())

    class Meta:
        model = List
        fields = ['id', 'name', 'description', 'user',
                  'created_at', 'updated_at']


class ListItemSerializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.PrimaryKeyRelatedField(
            queryset=List.objects.all())

    class Meta:
        model = ListItem
        fields = ['id', 'text', 'parent_list',
                  'created_at', 'updated_at']


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class ListItemViewSet(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer
