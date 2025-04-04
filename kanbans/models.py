from django.db import models
from django.contrib.auth import get_user_model


class Kanban(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    assignees = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1)


class KanbanField(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    position = models.IntegerField()
    kanban = models.ForeignKey('kanbans.Kanban', on_delete=models.CASCADE)
