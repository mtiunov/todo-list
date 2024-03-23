from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "published_date", "deadline", ]
    search_fields = ["content", ]


admin.site.register(Tag)
