from django.db import models
from django.contrib.auth import get_user_model

from apps.utils.models import Timestamps
from apps.projects.models import Project


class Task(Timestamps, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING,
                                null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    completed = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)

    CATEGORIES = (
        (1, 'inbox'),
        (2, 'next'),
        (3, 'maybe'),
        (4, 'project')
    )
    category = models.IntegerField(choices=CATEGORIES, default=1)

    def __str__(self):
        return self.title

    # def tags(self):
    #     return self.tags...


class Tag(models.Model):
    text = models.CharField(max_length=25)
    color = models.CharField(max_length=6, default='424244')
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return self.text
