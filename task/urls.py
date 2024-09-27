from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    path("", views.AllTasks, name="show_tasks"),
    path("add_task/", views.ShowAddTaskForm, name="add_task_form"),
]
