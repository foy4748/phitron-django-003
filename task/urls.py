from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    path("", views.AllTasks, name="show_tasks"),
    path("add_task/", views.ShowAddTaskForm, name="add_task_form"),
    path("edit_task/<str:pk>/", views.ShowEditTaskForm, name="edit_task_form"),
    path("delete_task/<str:pk>/", views.DeleteSingleTask, name="delete_task"),
]
