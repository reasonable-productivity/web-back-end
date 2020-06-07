from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import Timestamps


class List(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class ListItem(Timestamps, models.Model):
    parent_list = models.ForeignKey(List, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
