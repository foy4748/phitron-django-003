from django.db import models


# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
