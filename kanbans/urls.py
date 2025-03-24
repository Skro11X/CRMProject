from django.urls import path
from kanbans.views import KanbanDetail

urlpatterns = [
    path('<int:id>/', KanbanDetail.as_view(), name="kanban_detail"),
]