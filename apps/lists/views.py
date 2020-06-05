from rest_framework import serializers, viewsets
from .models import List


class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ['name', 'description', 'user_id',
                  'created_at', 'updated_at']


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
