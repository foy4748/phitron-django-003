from django.db import models


# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length=255)
