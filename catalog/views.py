from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag


def index(request):
    """View function for the home page of the site."""
    tasks = Task.objects.all()
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "tasks": tasks,
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }

    return render(request, "catalog/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "catalog/tag_list.html"
