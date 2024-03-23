from django.shortcuts import render
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
