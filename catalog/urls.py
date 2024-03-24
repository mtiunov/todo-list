from django.urls import path
from catalog.views import (
    index,
    TagListView,
    TaskCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),

]

app_name = "catalog"
