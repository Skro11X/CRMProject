from django.contrib import admin
from kanbans.models import Kanban, KanbanField


@admin.register(Kanban)
class KanbanAdmin(admin.ModelAdmin):
    pass


@admin.register(KanbanField)
class KanbanFieldAdmin(admin.ModelAdmin):
    pass
# Register your models here.
