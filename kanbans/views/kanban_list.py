from django.views.generic import ListView
from kanbans.models import Kanban


class KanbanList(ListView):
    model = Kanban
    template_name = "kanban_lists.html"
    context_object_name = "kanbans_list"