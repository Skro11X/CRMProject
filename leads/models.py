from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    kanban_field = models.ForeignKey("kanbans.KanbanField", on_delete=models.SET_DEFAULT, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    added = models.DateTimeField(auto_now=True)
