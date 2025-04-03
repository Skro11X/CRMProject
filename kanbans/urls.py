from django.urls import path
from kanbans.views import KanbanDetail, KanbanList

urlpatterns = [
    path('<int:id>/', KanbanDetail.as_view(), name="kanban_detail"),
    path('list/', KanbanList.as_view(), name="kanban_list")
]