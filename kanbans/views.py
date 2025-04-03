from django.views.generic import DetailView, ListView
from kanbans.models import Kanban
from leads.models import Lead


class KanbanDetail(DetailView):
    template_name = "kanban_detail.html"
    context_object_name = 'list_kanban_leads'
    pk_url_kwarg = "id"

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        list_of_leads = Lead.objects.select_related('kanban_field__kanban').filter(kanban_field__kanban=pk)
        kanban_columns = {}
        for lead in list_of_leads:
            kanban_columns.setdefault(lead.kanban_field.position).append(lead)
        return kanban_columns


class KanbanList(ListView):
    model = Kanban
    template_name = "kanban_lists.html"
    context_object_name = "kanbans_list"
