from django.db import models
from django.utils import timezone
from category.models import TaskCategory


# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=255)
    task_description = models.CharField(max_length=1023)
    is_completed = models.BooleanField(default=False)  # type: ignore
    task_assign_date = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(TaskCategory, related_name="tasks")
