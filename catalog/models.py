from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(verbose_name="deadline", blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["deadline", "-published_date"]

    def __str__(self):
        return f"{self.content} ({self.published_date} {self.tags})"
