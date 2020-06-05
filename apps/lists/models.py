from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import Timestamps


class List(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
